# Changelog

## v2026.10.1 - 2026-10-16

- Changed: the version is no longer part of the blueprint name; it is in the description.
  Spook's update entity takes its entity ID from the name, so a version there would stay frozen
  in the entity ID after updates.

## v2026.10.0 - 2026-10-16

First release in this repository.

- Added: every trigger, condition and action has a name, so traces show which button and
  event was handled.
- Added: `author`, `min_version` (2024.6.0) and `source_url`.
