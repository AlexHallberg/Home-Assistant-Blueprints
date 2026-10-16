# Changelog

## v2026.10.0 - 2026-10-16

First release in this repository.

- Fixed: a Hue bridge reconnect no longer replays each button's last event. Triggers now
  ignore changes to and from `unavailable` and `unknown`.
- Added: every trigger, condition and action has a name, so traces show which button and
  event was handled.
- Added: `author`, `min_version` (2023.8.0) and `source_url`.
- Inputs are unchanged, so existing automations keep their settings.
