# Upstream

This blueprint is a fork of
[edwardtfn/ha_auto_update_scheduled](https://github.com/edwardtfn/ha_auto_update_scheduled)
by [Edward Firmo](https://github.com/edwardtfn).

## License

Upstream does not publish a license. The MIT license at the root of this repository
does **not** apply to this folder; the original work remains Edward Firmo's.

## Sync state

| Field            | Value                                              |
| ---------------- | -------------------------------------------------- |
| Imported with    | `git subtree add` (full history)                   |
| Upstream commit  | `1924a7f` (Merge pull request #22 from edwardtfn/dev) |
| Upstream version | v2026.6.0                                          |
| Fork version     | v2026.10.1 (see [CHANGELOG.md](CHANGELOG.md))      |

## Changes in this fork

- `source_url` and the README import badge point at this repository.
- A fork notice was added to the file header, the blueprint description and the README.
- Every condition and action has an `alias`, so traces show readable step names. Repeated
  conditions and notification steps are shared through YAML anchors.
- New optional install log and error log (File integration notify entities), with the
  `install_log_section` inputs.
- Fixed: the "Update process started" toggle was treated as a list, but the entity
  selector gives a plain string, so `count` and `first` returned its length and first
  character. Resume after a restart was never detected, and with the toggle set the
  backup was always skipped. The input is now normalised once into
  `update_process_toggle`, and the "No backup has been made yet" check uses the
  toggle's state at the start of the run, since "Set ON helper flag" turns it on
  before the backup step.
- Upstream's `.github` and `.rules` folders were moved to the repository root.

Because of the aliases, almost every block in the blueprint differs from upstream, so
`git subtree pull` will conflict heavily. Expect to port upstream fixes by hand.

## Pulling upstream changes

From the repository root:

```bash
git remote add upstream-auto-update https://github.com/edwardtfn/ha_auto_update_scheduled.git
git subtree pull --prefix=blueprints/automation/system/auto_update_scheduled upstream-auto-update main
```

`source_url` and the badge URL will conflict whenever upstream changes those lines;
keep this repository's URLs. Upstream changes to `.github` or `.rules` arrive as
modify/delete conflicts, since those folders were moved out; resolve them by
deleting the files again and porting anything useful to the root copies.
Update the sync table above after each pull.
