#!/usr/bin/env python3
"""Generate and sync the roadmap's GitHub issues from roadmap/.

    roadmap/stages/<stage>.toml       technical content, always in English:
                                      titles, topics, examples, resources
    roadmap/i18n/<lang>/ui.toml       issue headings and labels
    roadmap/i18n/<lang>/<stage>.toml  explanations: summary, goals, exercises,
                                      self-check, exam

Each issue carries a hidden marker (<!-- roadmap-id: ... -->) so re-running
updates the same issues instead of creating duplicates.

Usage:
    python3 scripts/sync_issues.py --check                 # validate every locale
    python3 scripts/sync_issues.py --preview --lang pt     # print issues, no GitHub
    python3 scripts/sync_issues.py --lang pt               # dry run against GitHub
    python3 scripts/sync_issues.py --lang pt --apply       # create / update issues

Requires Python 3.11+ and an authenticated GitHub CLI (`gh auth login`).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent.parent
STAGES = ROOT / "roadmap" / "stages"
I18N = ROOT / "roadmap" / "i18n"
BASE_LANG = "en"

MARKER = "<!-- roadmap-id: {} -->"
MARKER_RE = re.compile(r"<!-- roadmap-id: (\S+) -->")

LABEL_COLORS = {"epic": "FBCA04", "task": "0E8A16", "test": "D93F0B", "stage": "1D76DB"}

STAGE_KEYS = ("title", "months", "studies", "projects", "task")
TASK_KEYS = ("id", "title", "topics", "example")
TEXT_STAGE_KEYS = ("summary", "exam")
TEXT_TASK_KEYS = ("goals", "exercises", "check")


# ─── Loading ──────────────────────────────────────────────────────────────────

def merge(base: dict, override: dict) -> dict:
    out = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = merge(out[key], value)
        else:
            out[key] = value
    return out


def load_toml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("rb") as f:
        return tomllib.load(f)


def available_langs() -> list[str]:
    return sorted(p.name for p in I18N.iterdir() if p.is_dir())


def stage_files() -> list[Path]:
    return sorted(STAGES.glob("*.toml"))


def load_text(lang: str, name: str) -> dict:
    """Text for `name` (ui or a stage file) in `lang`, falling back to English."""
    if lang not in available_langs():
        sys.exit(f"Unknown language '{lang}'. Available: {', '.join(available_langs())}")
    base = load_toml(I18N / BASE_LANG / f"{name}.toml")
    return base if lang == BASE_LANG else merge(base, load_toml(I18N / lang / f"{name}.toml"))


# ─── Model ────────────────────────────────────────────────────────────────────

@dataclass
class Item:
    id: str
    kind: str  # epic | task | test
    title: str
    labels: list[str]
    render: Callable[[dict[str, str]], str] = field(repr=False)


def bullets(lines: list[str], checkbox: bool = False) -> list[str]:
    prefix = "- [ ] " if checkbox else "- "
    return [prefix + line for line in lines]


def section(heading: str, *body: str) -> list[str]:
    return [f"### {heading}", *body, ""]


def build_items(lang: str) -> list[Item]:
    ui = load_text(lang, "ui")["ui"]
    items: list[Item] = []

    for n, path in enumerate(stage_files(), start=1):
        stage = load_toml(path)
        text = load_text(lang, path.stem)
        sid = stage["id"]
        months = ui["months"].format(months=stage["months"])
        studies = stage["studies"]
        projects = " / ".join(f"`{p}/`" for p in stage["projects"])
        folders = " · ".join(f"`{f}/`" for f in [studies, *stage["projects"]])
        stage_label = f"stage-{n}"
        task_ids = [f"{sid}.{task['id']}" for task in stage["task"]]
        test_id = f"{sid}.test"
        header = f"**{ui['stage'].format(n=n)} — {stage['title']}** · {months}"
        resources = [f"[{r['title']}]({r['url']})" for r in stage.get("resources", [])]

        def epic_body(num, sid=sid, text=text, folders=folders, resources=resources,
                      children=task_ids + [test_id]):
            return "\n".join([
                text["summary"],
                "",
                f"**{ui['folders']}:** {folders}",
                "",
                *section(ui["tasks"], *[f"- [ ] {num[c]}" for c in children]),
                *(section(ui["resources"], *bullets(resources)) if resources else []),
                *section(ui["done_when"], *bullets(ui["epic_done"], checkbox=True)),
                MARKER.format(sid),
            ])

        items.append(Item(
            id=sid, kind="epic",
            title=ui["epic_title"].format(n=n, title=stage["title"], months=months),
            labels=["epic", stage_label], render=epic_body,
        ))

        for task, tid in zip(stage["task"], task_ids):
            tt = text.get("task", {}).get(task["id"], {})

            def task_body(num, sid=sid, tid=tid, task=task, tt=tt, header=header,
                          studies=studies, projects=projects):
                deliverables = [line.format(studies=studies, projects=projects)
                                for line in ui["task_done"]]
                return "\n".join([
                    f"{header} · {ui['part_of'].format(epic=num[sid])}",
                    "",
                    *section(ui["topics"], *bullets(task["topics"])),
                    *section(ui["goals"], *bullets(tt["goals"])),
                    *section(ui["example"], task["example"].strip()),
                    *section(ui["exercises"], *bullets(tt["exercises"], checkbox=True)),
                    *section(ui["check"], *bullets(tt["check"], checkbox=True)),
                    *section(ui["deliverables"], *bullets(deliverables, checkbox=True)),
                    MARKER.format(tid),
                ])

            items.append(Item(
                id=tid, kind="task",
                title=ui["task_title"].format(n=n, title=task["title"]),
                labels=["task", stage_label], render=task_body,
            ))

        def test_body(num, sid=sid, test_id=test_id, text=text, header=header, studies=studies):
            wrap_up = [line.format(studies=studies) for line in ui["test_wrap_up"]]
            return "\n".join([
                f"{header} · {ui['part_of'].format(epic=num[sid])}",
                "",
                ui["test_intro"],
                "",
                *section(ui["exam"], *bullets(text["exam"], checkbox=True)),
                *section(ui["wrap_up"], *bullets(wrap_up, checkbox=True)),
                ui["test_criterion"],
                "",
                MARKER.format(test_id),
            ])

        items.append(Item(
            id=test_id, kind="test",
            title=ui["test_title"].format(n=n, title=stage["title"]),
            labels=["test", stage_label], render=test_body,
        ))

    return items


def build_labels(lang: str) -> dict[str, tuple[str, str]]:
    names = load_text(lang, "ui")["labels"]
    labels = {kind: (LABEL_COLORS[kind], names[kind]) for kind in ("epic", "task", "test")}
    for n, path in enumerate(stage_files(), start=1):
        desc = names["stage"].format(n=n, title=load_toml(path)["title"])
        labels[f"stage-{n}"] = (LABEL_COLORS["stage"], desc)
    return labels


# ─── Validation ───────────────────────────────────────────────────────────────

def check() -> int:
    errors: list[str] = []
    ui_keys = list(load_toml(I18N / BASE_LANG / "ui.toml").get("ui", {}))
    required: dict[str, list[tuple[str, ...]]] = {
        "ui": [("ui", k) for k in ui_keys] + [("labels", k) for k in ("epic", "task", "test", "stage")],
    }

    for path in stage_files():
        stage = load_toml(path)
        errors += [f"stages/{path.name}: missing '{k}'" for k in STAGE_KEYS if k not in stage]
        for task in stage.get("task", []):
            errors += [f"stages/{path.name}: task {task.get('id', '?')} missing '{k}'"
                       for k in TASK_KEYS if k not in task]
        required[path.stem] = [(k,) for k in TEXT_STAGE_KEYS] + [
            ("task", task["id"], k) for task in stage.get("task", []) for k in TEXT_TASK_KEYS
        ]

    for lang in available_langs():
        missing = []
        for name, keys in required.items():
            data = load_toml(I18N / lang / f"{name}.toml")
            missing += [f"{name}: {'.'.join(k)}" for k in keys if lookup(data, k) is None]
        if not missing:
            print(f"✓ {lang}: complete")
        elif lang == BASE_LANG:
            errors += [f"i18n/{lang}/{m}" for m in missing]
        else:
            print(f"! {lang}: {len(missing)} key(s) fall back to '{BASE_LANG}'")
            for m in missing:
                print(f"    {m}")

    for e in errors:
        print(f"✗ {e}")
    return 1 if errors else 0


def lookup(data: dict, path: tuple[str, ...]):
    for key in path:
        if not isinstance(data, dict) or key not in data:
            return None
        data = data[key]
    return data


# ─── GitHub ───────────────────────────────────────────────────────────────────

def gh(*args: str, input: str | None = None) -> str:
    result = subprocess.run(["gh", *args], input=input, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"gh {' '.join(args[:3])} failed:\n{result.stderr.strip()}")
    return result.stdout


def repo_args(repo: str | None) -> list[str]:
    return ["--repo", repo] if repo else []


def fetch_issues(repo: str | None) -> list[dict]:
    out = gh("issue", "list", *repo_args(repo), "--state", "all", "--limit", "1000",
             "--json", "number,title,body,labels")
    return json.loads(out)


def sync(lang: str, repo: str | None, apply: bool, map_file: Path | None) -> None:
    items = build_items(lang)
    labels = build_labels(lang)
    issues = {i["number"]: i for i in fetch_issues(repo)}

    by_id: dict[str, dict] = {}
    for issue in issues.values():
        if m := MARKER_RE.search(issue["body"] or ""):
            by_id[m.group(1)] = issue
    if map_file:
        for rid, number in json.loads(map_file.read_text()).items():
            if number not in issues:
                sys.exit(f"{map_file}: issue #{number} (for '{rid}') not found")
            by_id.setdefault(rid, issues[number])

    mode = "APPLY" if apply else "DRY RUN (add --apply to make changes)"
    print(f"{mode} · lang={lang} · {len(items)} roadmap items · {len(by_id)} already linked\n")

    print(f"labels  {', '.join(labels)}")
    if apply:
        for name, (color, desc) in labels.items():
            gh("label", "create", name, *repo_args(repo), "--color", color,
               "--description", desc, "--force")

    numbers: dict[str, str] = {}
    for item in items:
        if item.id in by_id:
            numbers[item.id] = f"#{by_id[item.id]['number']}"
            continue
        print(f"create  {item.title}")
        if apply:
            url = gh("issue", "create", *repo_args(repo), "--title", item.title,
                     "--body", MARKER.format(item.id), *sum([["--label", l] for l in item.labels], []))
            number = int(url.strip().rsplit("/", 1)[-1])
            by_id[item.id] = {"number": number, "title": item.title, "body": "", "labels": []}
            numbers[item.id] = f"#{number}"
        else:
            numbers[item.id] = "#?"

    for item in items:
        issue = by_id.get(item.id)
        if issue is None:
            continue
        body = item.render(numbers)
        current = {l["name"] for l in issue["labels"]}
        add = [l for l in item.labels if l not in current]
        changes = [what for what, changed in (
            ("title", issue["title"] != item.title),
            ("body", (issue["body"] or "").strip() != body.strip()),
            ("labels", bool(add)),
        ) if changed]
        if not changes:
            continue
        print(f"update  #{issue['number']} {item.title}  [{', '.join(changes)}]")
        if apply:
            gh("issue", "edit", str(issue["number"]), *repo_args(repo), "--title", item.title,
               "--body-file", "-", *sum([["--add-label", l] for l in add], []), input=body)

    print("\ndone." if apply else "\nNothing was changed.")


def preview(lang: str, only: str | None) -> None:
    items = build_items(lang)
    numbers = {item.id: f"#<{item.id}>" for item in items}
    shown = [i for i in items if only is None or i.id == only or i.id.startswith(f"{only}.")]
    for item in shown:
        print(f"{'═' * 80}\n{item.title}\nlabels: {', '.join(item.labels)}\n{'─' * 80}")
        print(item.render(numbers))
    print(f"{'═' * 80}\n{len(shown)} issues")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lang", default=BASE_LANG, help=f"issue language: {', '.join(available_langs())}")
    parser.add_argument("--repo", help="OWNER/REPO (default: the current repo)")
    parser.add_argument("--check", action="store_true", help="validate stages and locales, then exit")
    parser.add_argument("--preview", nargs="?", const="", metavar="ID",
                        help="print rendered issues (optionally only one id or stage, e.g. s1 or s1.vectors)")
    parser.add_argument("--apply", action="store_true", help="actually create / update issues")
    parser.add_argument("--map", type=Path, metavar="FILE",
                        help='JSON {"roadmap-id": issue_number} to adopt issues created without markers')
    args = parser.parse_args()

    if args.check:
        sys.exit(check())
    if args.preview is not None:
        preview(args.lang, args.preview or None)
    else:
        sync(args.lang, args.repo, args.apply, args.map)


if __name__ == "__main__":
    main()
