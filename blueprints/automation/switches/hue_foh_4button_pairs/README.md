# Hue - Friends of Hue switch, 4 button pairs

Controls lights from one 4-button Friends of Hue switch connected through the Hue bridge.
The buttons work as two on/off pairs, and holding a button dims or brightens.

For your own actions on every button and event, or several switches in one automation, see
[Friends of Hue 4-button custom](../hue_foh_4button_custom/).

Its custom-action inputs are based on the "all functions" blueprint by
[Khvej8](https://community.home-assistant.io/u/khvej8) from the
[Home Assistant Community thread](https://community.home-assistant.io/t/499450/32).

| Pair | On / hold to brighten   | Off / hold to dim       |
| ---- | ----------------------- | ----------------------- |
| 1    | Button 1 (upper left)   | Button 3 (upper right)  |
| 2    | Button 2 (lower left)   | Button 4 (lower right)  |

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.][import-badge]][import]

[import-badge]: https://my.home-assistant.io/badges/blueprint_import.svg
[import]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Fswitches%2Fhue_foh_4button_pairs%2Fhue_foh_4button_pairs.yaml

## How it works

Each run starts on a button's `initial_press` and then follows only that button until it is released:

- **Short press:** turns the pair's lights on or off on `short_release`.
- **Hold:** steps brightness up or down on every `repeat` event, and finishes on `long_release`.

Friends of Hue switches can send a `short_release` straight after a `long_release`. The run has
already ended at the long release, so that stray event can't toggle the lights.

Events from other buttons are ignored while a button is held. If no release arrives within the
release timeout, the run gives up.

## Inputs

- **Switch:** the Friends of Hue device, selected from the Hue integration.
- **Pair 1 / Pair 2:** the lights for each pair, or **Use custom actions** to run your own actions
  for that pair instead.
- **Options:** dim step per repeat (%), on/off transition (s), and the release timeout (s).
- **Custom actions:** press, repeat, short release and long release actions for each of the four
  buttons. These are only used for a pair that has **Use custom actions** turned on.

## Requirements

- Home Assistant 2024.6 or newer.
- The switch must be paired with a Hue bridge and added through the Hue integration, which
  provides the `hue_event` events this blueprint listens to.
