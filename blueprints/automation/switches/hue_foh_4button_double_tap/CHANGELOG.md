# Changelog

## v2026.10.1 - 2026-10-16

- Changed: select one Friends of Hue switch device instead of an event entity per button. Its
  buttons are mapped automatically from the Hue integration's `hue_event` events.
  **Breaking:** automations made from v2026.10.0 need the switch selected again.
- Removed: several switches in one automation. Use one automation per switch.

## v2026.10.0 - 2026-10-16

First release.

- Single click, double click, hold (repeating) and hold-release actions for each of the four
  buttons. A double click runs only the double-click action.
- Only buttons ticked as having a double-click action wait for the double-click window.
- No helpers needed: one run follows each button sequence.
- Triggers ignore changes to and from `unavailable` and `unknown`.
- Every trigger, condition and action is named for readable traces.
