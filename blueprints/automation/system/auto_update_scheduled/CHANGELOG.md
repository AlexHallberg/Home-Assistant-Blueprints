# Changelog

Versions before v2026.10.0 are upstream releases; see the
[upstream commit log](https://github.com/edwardtfn/ha_auto_update_scheduled/commits/main).

## v2026.10.1 - 2026-10-16

- Changed: renamed to "Home Assistant Auto-update".
- Fixed: with no schedule entity set, the install log said "(the schedule ended)" on every
  "not installed" entry.
- Changed: the schedule entity input says it can be left empty to install updates whenever they
  are found, and the "Schedule is on" trace steps now read "(or no schedule is set)".
- Changed: the version is no longer part of the blueprint name; it is in the description.
  Spook's update entity takes its entity ID from the name, so a version there would stay frozen
  in the entity ID after updates.

## v2026.10.0 - 2026-10-16

First release of this fork, based on upstream v2026.6.0 (`1924a7f`).

- Added: every condition and action has a name, so traces show why a run stopped.
- Added: optional install log and error log files (File integration notify entities).
- Fixed: the "Update process started" toggle was handled as a list, so resuming after a
  restart was never detected and, with the toggle set, the backup was always skipped.
- Changed: `source_url` and the import badge point at this repository.
