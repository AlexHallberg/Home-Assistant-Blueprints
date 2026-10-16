# Hue - Friends of Hue switch, 4 button, custom actions

Runs your own actions for every button and event on Friends of Hue 4-button switches connected
through the Hue bridge: initial press, repeat (held), short release and long release, for each
of the four buttons. One automation can drive several switches the same way.

For built-in on/off and dimming of lights, see
[Friends of Hue 4-button pairs](../hue_foh_4button_pairs/).

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.][import-badge]][import]

[import-badge]: https://my.home-assistant.io/badges/blueprint_import.svg
[import]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Fswitches%2Fhue_foh_4button_custom%2Fhue_foh_4button_custom.yaml

## How it works

Each Hue button is an event entity. The blueprint triggers on that entity's state changes and
reads the event type:

- **Initial press, repeat, long release:** runs that button's action.
- **Short release:** runs only if the button's previous event was its initial press. Friends of
  Hue switches can send a `short_release` straight after a `long_release`; that stray event
  follows a hold, so it is ignored.

Events are handled one at a time in order (`mode: queued`, up to 10 waiting).

Triggers ignore changes to and from `unavailable` and `unknown`. Without that, a Hue bridge
reconnect would bring each button back with its last event and run that action again.

## Inputs

- **Hue Switch button 1-4:** the event entity for each button. Select the same button on
  several switches to give them the same actions.
- **Press, Repeat, Short Release, Long Release 1-4:** the actions for each button and event.
  Leave any of them empty to do nothing.

## Requirements

- Home Assistant 2023.8 or newer.
- The switch must be paired with a Hue bridge and added through the Hue integration, which
  provides one event entity per button.
