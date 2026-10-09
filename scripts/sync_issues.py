#!/usr/bin/env python3
"""Generate and sync the roadmap's GitHub issues from roadmap/.

    roadmap/roadmap.toml      structure (stages, task ids, folders)
    roadmap/i18n/<lang>.toml  all text, one file per language

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
ROADMAP = ROOT / "roadmap" / "roadmap.toml"
I18N = ROOT / "roadmap" / "i18n"
BASE_LANG = "en"

MARKER = "<!-- roadmap-id: {} -->"
MARKER_RE = re.compile(r"<!-- roadmap-id: (\S+) -->")

LABEL_COLORS = {"epic": "FBCA04", "task": "0E8A16", "test": "D93F0B", "stage": "1D76DB"}


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
    with path.open("rb") as f:
        return tomllib.load(f)


def available_langs() -> list[str]:
    return sorted(p.stem for p in I18N.glob("*.toml"))


def load_locale(lang: str) -> dict:
    path = I18N / f"{lang}.toml"
    if not path.exists():
        sys.exit(f"Unknown language '{lang}'. Available: {', '.join(available_langs())}")
    base = load_toml(I18N / f"{BASE_LANG}.toml")
    return base if lang == BASE_LANG else merge(base, load_toml(path))


# ─── Model ────────────────────────────────────────────────────────────────────

@dataclass
class Item:
    id: str
    kind: str  # epic | task | test
    stage: int
    title: str
    labels: list[str]
    render: Callable[[dict[str, str]], str] = field(repr=False)  # (numbers: dict[str, str]) -> body


def build_items(lang: str) -> list[Item]:
    roadmap = load_toml(ROADMAP)
    t = load_locale(lang)
    ui = t["ui"]
    items: list[Item] = []

    for n, stage in enumerate(roadmap["stage"], start=1):
        sid = stage["id"]
        st = t["stage"][sid]
        months = ui["months"].format(months=stage["months"])
        studies = stage["studies"]
        projects = " / ".join(f"`{f}/`" for f in stage["projects"])
        folders = " · ".join(f"`{f}/`" for f in [stage["studies"], *stage["projects"]])
        stage_label = f"stage-{n}"
        task_ids = [f"{sid}.{task}" for task in stage["tasks"]]
        test_id = f"{sid}.test"
        header = f"**{ui['stage'].format(n=n)} — {st['title']}** · {months}"

        def epic_body(num, sid=sid, st=st, folders=folders,
                      children=task_ids + [test_id]):
            return "\n".join([
                st["summary"],
                "",
                f"**{ui['folders']}:** {folders}",
                "",
                f"### {ui['tasks']}",
                *[f"- [ ] {num[c]}" for c in children],
                "",
                f"### {ui['done_when']}",
                *[f"- [ ] {line}" for line in ui["epic_done"]],
                "",
                MARKER.format(sid),
            ])

        items.append(Item(
            id=sid, kind="epic", stage=n,
            title=ui["epic_title"].format(n=n, title=st["title"], months=months),
            labels=["epic", stage_label], render=epic_body,
        ))

        for task, tid in zip(stage["tasks"], task_ids):
            tt = st["task"][task]

            def task_body(num, sid=sid, tid=tid, tt=tt, header=header, studies=studies, projects=projects):
                return "\n".join([
                    header,
                    "",
                    f"### {ui['study']}",
                    tt["study"],
                    "",
                    f"### {ui['practice']}",
                    tt["practice"],
                    "",
                    f"### {ui['done_when']}",
                    *[f"- [ ] {line.format(studies=studies, projects=projects)}"
                      for line in ui["task_done"]],
                    "",
                    ui["part_of"].format(epic=num[sid]),
                    "",
                    MARKER.format(tid),
                ])

            items.append(Item(
                id=tid, kind="task", stage=n,
                title=ui["task_title"].format(n=n, title=tt["title"]),
                labels=["task", stage_label], render=task_body,
            ))

        def test_body(num, sid=sid, test_id=test_id, st=st, header=header, studies=studies):
            return "\n".join([
                header,
                "",
                ui["test_intro"],
                "",
                *[f"- [ ] {line.format(studies=studies, challenge=st['challenge'])}"
                  for line in ui["test_steps"]],
                "",
                ui["test_criterion"],
                "",
                ui["part_of"].format(epic=num[sid]),
                "",
                MARKER.format(test_id),
            ])

        items.append(Item(
            id=test_id, kind="test", stage=n,
            title=ui["test_title"].format(n=n, title=st["title"]),
            labels=["test", stage_label], render=test_body,
        ))

    return items


def build_labels(lang: str) -> dict[str, tuple[str, str]]:
    roadmap = load_toml(ROADMAP)
    t = load_locale(lang)
    labels = {kind: (LABEL_COLORS[kind], t["labels"][kind]) for kind in ("epic", "task", "test")}
    for n, stage in enumerate(roadmap["stage"], start=1):
        desc = t["labels"]["stage"].format(n=n, title=t["stage"][stage["id"]]["title"])
        labels[f"stage-{n}"] = (LABEL_COLORS["stage"], desc)
    return labels


# ─── Validation ───────────────────────────────────────────────────────────────

def required_keys(roadmap: dict) -> list[tuple[str, ...]]:
    keys = [("ui", k) for k in load_toml(I18N / f"{BASE_LANG}.toml")["ui"]]
    keys += [("labels", k) for k in ("epic", "task", "test", "stage")]
    for stage in roadmap["stage"]:
        sid = stage["id"]
        keys += [("stage", sid, k) for k in ("title", "summary", "challenge")]
        for task in stage["tasks"]:
            keys += [("stage", sid, "task", task, k) for k in ("title", "study", "practice")]
    return keys


def lookup(data: dict, path: tuple[str, ...]):
    for key in path:
        if not isinstance(data, dict) or key not in data:
            return None
        data = data[key]
    return data


def check() -> int:
    roadmap = load_toml(ROADMAP)
    keys = required_keys(roadmap)
    errors = 0
    for lang in available_langs():
        raw = load_toml(I18N / f"{lang}.toml")
        missing = [".".join(k) for k in keys if lookup(raw, k) is None]
        if not missing:
            print(f"✓ {lang}: complete")
        elif lang == BASE_LANG:
            errors += len(missing)
            print(f"✗ {lang}: {len(missing)} missing key(s) — the base locale must be complete")
            for k in missing:
                print(f"    {k}")
        else:
            print(f"! {lang}: {len(missing)} key(s) fall back to '{BASE_LANG}'")
            for k in missing:
                print(f"    {k}")
    return 1 if errors else 0


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


def preview(lang: str) -> None:
    items = build_items(lang)
    numbers = {item.id: f"#<{item.id}>" for item in items}
    for item in items:
        print(f"{'═' * 80}\n{item.title}\nlabels: {', '.join(item.labels)}\n{'─' * 80}")
        print(item.render(numbers))
    print(f"{'═' * 80}\n{len(items)} issues")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lang", default=BASE_LANG, help=f"issue language: {', '.join(available_langs())}")
    parser.add_argument("--repo", help="OWNER/REPO (default: the current repo)")
    parser.add_argument("--check", action="store_true", help="validate locales and exit")
    parser.add_argument("--preview", action="store_true", help="print rendered issues, no GitHub")
    parser.add_argument("--apply", action="store_true", help="actually create / update issues")
    parser.add_argument("--map", type=Path, metavar="FILE",
                        help='JSON {"roadmap-id": issue_number} to adopt issues created without markers')
    args = parser.parse_args()

    if args.check:
        sys.exit(check())
    if args.preview:
        preview(args.lang)
    else:
        sync(args.lang, args.repo, args.apply, args.map)


if __name__ == "__main__":
    main()
