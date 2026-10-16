# Changelog

Versions before v2026.10.0 are upstream releases; see the
[upstream commit log](https://github.com/edwardtfn/ha_auto_update_scheduled/commits/main).

## v2026.10.0 - 2026-10-16

First release of this fork, based on upstream v2026.6.0 (`1924a7f`).

- Added: every condition and action has a name, so traces show why a run stopped.
- Added: optional install log and error log files (File integration notify entities).
- Fixed: the "Update process started" toggle was handled as a list, so resuming after a
  restart was never detected and, with the toggle set, the backup was always skipped.
- Changed: `source_url` and the import badge point at this repository.
