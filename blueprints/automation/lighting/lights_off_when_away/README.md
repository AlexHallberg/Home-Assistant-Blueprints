# Turn off lights when nobody is home

Once a day, at a time you choose (default 03:00), turns off the selected lights if nobody is home.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.][import-badge]][import]

[import-badge]: https://my.home-assistant.io/badges/blueprint_import.svg
[import]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Flighting%2Flights_off_when_away%2Flights_off_when_away.yaml

## Inputs

| Input | What it does |
| ----- | ------------ |
| People | People, device trackers or a group of them. Lights are turned off only when none of them is `home`. |
| Lights to turn off | Floors, areas, labels or individual lights. |
| Time | When to check every day. Default 03:00. |

## How "nobody is home" is decided

- Anything other than `home` counts as away, so `not_home`, `away` and zone names all count.
- For a group, the group's own state is used.
- If any selected entity is `unknown` or `unavailable`, nothing is turned off. It is not certain
  the house is empty, for example right after a restart.

## Example

The same blueprint works in each house; only the inputs differ:

```yaml
alias: Turn off all lights if nobody home
use_blueprint:
  path: AlexHallberg/lights_off_when_away.yaml
  input:
    presence_entities:
      - group.persons
    lights:
      floor_id:
        - main
        - outside
      area_id: attic
    check_time: "03:00:00"
```
