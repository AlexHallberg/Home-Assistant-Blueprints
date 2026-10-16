# Hue - Friends of Hue switch, 4 button, single + double click + hold

Gives each button on a Friends of Hue 4-button switch (connected through the Hue bridge) up to
four actions:

| You do                       | It runs                                                   |
| ---------------------------- | --------------------------------------------------------- |
| 1 click                      | Single-click action only                                  |
| 2 quick clicks               | Double-click action only                                  |
| Hold                         | Hold action on every repeat (about every 0.8 s) — dimming |
| Let go after holding         | Hold-release action                                       |
| Click, then hold             | Counts as a hold                                          |

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.][import-badge]][import]

[import-badge]: https://my.home-assistant.io/badges/blueprint_import.svg
[import]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Fswitches%2Fhue_foh_4button_double_tap%2Fhue_foh_4button_double_tap.yaml

Inspired by Anybody4u's [multi tap v2](https://gist.github.com/Anybody4u/304fbb8f6d5d82b417dda7dbbf2cf5cb),
rebuilt so a double click runs only its own action and no counter helpers are needed.

## Setup

1. Select the switch. Its four buttons are mapped automatically. Use one automation per switch.
2. Fill in the actions for each button. Leave any of them empty to do nothing.
3. Under **Double click and timing**, tick the buttons that have a double-click action.

Only ticked buttons wait before a single click runs, because they must see whether a second
click follows. Buttons that are not ticked run their single-click action straight away.

## Dimming example

Hold to brighten on one button and hold to dim on another:

```yaml
# Hold action, brighten
action: light.turn_on
target:
  entity_id: light.living_room
data:
  brightness_step_pct: 10
  transition: 0.5
```

```yaml
# Hold action, dim
action: light.turn_on
target:
  entity_id: light.living_room
data:
  brightness_step_pct: -10
  transition: 0.5
```

## Timing

- **Double-click window** (default 500 ms): how long after releasing the first click a second
  press still counts as a double click. It is also how long a single click waits on ticked buttons.
- **Release timeout** (default 30 s): a safety net in case a release event is lost.

## How it works

The blueprint listens to the Hue integration's `hue_event` events for the selected switch.
One run follows the whole sequence: the first press, its release, and a possible second press.
Because of that, the double-click decision needs no helpers.

- While a sequence is running, presses on the switch's *other* buttons are ignored
  (`mode: single`).
- A third quick click starts a new sequence, so a triple click runs the double-click action and
  then the single-click action.
- `hue_event` only fires for real button events, so a Hue bridge reconnect does not replay a
  button's last event.
- A hold ends on the first `long_release` or `short_release`, which covers Friends of Hue
  switches that send either or both.

## Requirements

- Home Assistant 2024.10 or newer.
- The switch must be paired with a Hue bridge and added through the Hue integration.
  Switches added through Zigbee2MQTT or ZHA are not supported.
