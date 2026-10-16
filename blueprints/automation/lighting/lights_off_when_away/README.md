# Turn off lights when nobody is home

Once a day, at a time you choose (default 03:00), turns off every light in Home Assistant if
nobody is home.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.][import-badge]][import]

[import-badge]: https://my.home-assistant.io/badges/blueprint_import.svg
[import]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Flighting%2Flights_off_when_away%2Flights_off_when_away.yaml

## Inputs

| Input | What it does |
| ----- | ------------ |
| Home zone | The zone whose person count decides whether anybody is home. Default `zone.home`. |
| Time | When to check every day. Default 03:00. |

## How "nobody is home" is decided

- A zone's state is the number of people in it, so nobody is home when the home zone is `0`.
- Only `person` entities are counted. A device tracker counts only through the person it belongs to.
- If the zone is `unknown` or `unavailable`, nothing is turned off. It is not certain the house is
  empty, for example right after a restart.

## Example

With the defaults, the same automation works in every house:

```yaml
alias: Turn off all lights if nobody home
use_blueprint:
  path: AlexHallberg/lights_off_when_away.yaml
  input: {}
```
