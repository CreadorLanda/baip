# Roadmap data

The roadmap's GitHub issues are **generated** from the files in this folder —
edit these files, not the issues.

```
roadmap/
├── stages/                technical content — always in English
│   ├── s1-math.toml       stage title, folders, resources,
│   └── …                  and per task: title, topics, worked example
└── i18n/                  explanations — one folder per language
    ├── en/                reference locale, must be complete
    │   ├── ui.toml        issue headings and label descriptions
    │   ├── s1-math.toml   summary, exam, and per task: goals, exercises, self-check
    │   └── …
    └── pt/                Português (same files)
```

**Why topics stay in English:** titles, topic names and worked examples are the
vocabulary of papers, docs and code. Keeping them in English in every language
means what you learn matches what you will read and search for. Everything that
*explains* — goals, exercises, self-checks, exams — is translated.

## What every issue contains

| Issue | Sections |
|-------|----------|
| **Epic** (one per stage) | summary · folders · task list · resources · done when |
| **Task** | 📚 topics · 🎯 goals · 💡 worked example · 🛠️ exercises (with answers) · 🧠 self-check · 📦 deliverables |
| **Final test** | 📝 exam problems · ✅ wrap-up · pass criterion |

## Create the issues in your own repo

1. Fork or copy this repository.
2. Install the [GitHub CLI](https://cli.github.com/) and run `gh auth login`.
3. Pick a language and run:

```bash
python3 scripts/sync_issues.py --lang en            # dry run: shows what would change
python3 scripts/sync_issues.py --lang en --apply    # creates labels + 9 epics, 40 tasks, 9 final tests
```

**Several languages in one issue:** pass a comma-separated list. The first
language is the main body (with the checkboxes); every other one is added as a
collapsible section with its translated goals, exercises and self-checks:

```bash
python3 scripts/sync_issues.py --lang pt,en --apply   # Portuguese + 🇬🇧 English
```

Re-running is safe: every issue has a hidden `<!-- roadmap-id: ... -->` marker,
so the script updates existing issues instead of duplicating them. Closed
issues stay closed — but re-running **overwrites the body**, so ticked
checkboxes are reset on issues whose text changed.

Other commands:

```bash
python3 scripts/sync_issues.py --check                       # validate stages and every locale
python3 scripts/sync_issues.py --preview --lang pt           # print all issues, no GitHub needed
python3 scripts/sync_issues.py --preview s1.vectors --lang pt  # print one issue (or a whole stage: s1)
```

## Change the roadmap

- **Edit text** → change it in `stages/` (technical) or `i18n/<lang>/` (explanations), then sync.
- **Add a task** → add a `[[task]]` with `id`, `title`, `topics` and `example`
  to the stage file, then a `[task.<id>]` with `goals`, `exercises` and `check`
  to `i18n/en/<stage>.toml` (and any other locale).
- **Add a stage** → add `stages/sN-name.toml` and `i18n/en/sN-name.toml`.
  Stages are ordered by file name.
- **Ids are permanent.** Renaming an id creates a new issue; the old one is left as is.

## Add a language

1. Copy `i18n/en/` to `i18n/<code>/` (e.g. `es/`, `fr/`).
2. Translate the values. Keep the keys and `{placeholders}` unchanged.
3. Run `python3 scripts/sync_issues.py --check`. Anything not translated yet falls back to English.

Label names (`epic`, `task`, `test`, `stage-N`) are the same in every language
so filters and links keep working; only their descriptions are translated.

## Adopt issues created by hand

If your repo already has roadmap issues without markers, link them once with a
JSON map of roadmap id → issue number:

```json
{ "s1": 1, "s1.vectors": 2, "s1.test": 13 }
```

```bash
python3 scripts/sync_issues.py --lang en --map map.json          # dry run
python3 scripts/sync_issues.py --lang en --map map.json --apply
```

After that the markers are in place and `--map` is no longer needed.
