# Roadmap data

The roadmap's GitHub issues are **generated** from the files in this folder —
edit these files, not the issues.

```
roadmap/
├── roadmap.toml     structure: stages, task ids, folders (no text)
└── i18n/
    ├── en.toml      English — reference locale, must be complete
    └── pt.toml      Português
```

## Create the issues in your own repo

1. Fork or copy this repository.
2. Install the [GitHub CLI](https://cli.github.com/) and run `gh auth login`.
3. Pick a language and run:

```bash
python3 scripts/sync_issues.py --lang en            # dry run: shows what would change
python3 scripts/sync_issues.py --lang en --apply    # creates labels + 9 epics, tasks and final tests
```

Re-running is safe: every issue has a hidden `<!-- roadmap-id: ... -->` marker,
so the script updates existing issues instead of duplicating them. Closed
issues stay closed.

Other commands:

```bash
python3 scripts/sync_issues.py --check              # validate every locale
python3 scripts/sync_issues.py --preview --lang pt  # print the issues, no GitHub needed
```

## Change the roadmap

- **Edit text** → change it in `i18n/<lang>.toml`, then sync.
- **Add a task** → add its id to the stage's `tasks` list in `roadmap.toml`,
  then add `[stage.<id>.task.<task>]` with `title`, `study` and `practice` to
  `i18n/en.toml` (and any other locale).
- **Ids are permanent.** Renaming an id creates a new issue; the old one is left
  as is.

## Add a language

1. Copy `i18n/en.toml` to `i18n/<code>.toml` (e.g. `es.toml`, `fr.toml`).
2. Translate the values. Keep the keys and `{placeholders}` unchanged.
3. Run `python3 scripts/sync_issues.py --check`. Anything you have not
   translated yet falls back to English.

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
