# Home Assistant Blueprints

A collection of Home Assistant blueprints: some written here, some forked from other
authors with local changes.

> [!IMPORTANT]
> These blueprints are built for my own Home Assistant setup. The repository is public
> so they are easy to import, and you are welcome to use them, but they are provided
> as is, without support or any guarantee they will work for you. Issues and feature
> requests may go unanswered, and things can change at any time. Review a blueprint
> before running it, especially the ones that update or restart your system.

## Blueprints

| Blueprint | Type | Category | Origin | Import |
| --------- | ---- | -------- | ------ | ------ |
| [Auto-update on a schedule](blueprints/automation/system/auto_update_scheduled/) | Automation | System | Fork of [edwardtfn][upstream-auto-update] | [![Import][import-badge]][import-auto-update] |
| [Hue Friends of Hue 4-button pairs](blueprints/automation/switches/hue_foh_4button_pairs/) | Automation | Switches | Own | [![Import][import-badge]][import-hue-foh] |

[import-badge]: https://my.home-assistant.io/badges/blueprint_import.svg
[upstream-auto-update]: https://github.com/edwardtfn/ha_auto_update_scheduled
[import-auto-update]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Fsystem%2Fauto_update_scheduled%2Fauto_update_scheduled.yaml
[import-hue-foh]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Fswitches%2Fhue_foh_4button_pairs%2Fhue_foh_4button_pairs.yaml

## Repository layout

```text
blueprints/
  <domain>/            automation, script or template, as in Home Assistant
    <category>/        what the blueprint does
      <name>/          one folder per blueprint
```

Categories in use, extended as new blueprints need them:

| Category        | For                                                |
| --------------- | -------------------------------------------------- |
| `system`        | Home Assistant itself: updates, backups, health    |
| `lighting`      | Lights and scenes                                  |
| `climate`       | Heating, cooling, ventilation                      |
| `presence`      | Occupancy, arriving and leaving                    |
| `security`      | Alarms, locks, cameras                             |
| `notifications` | Alerts and reminders                               |
| `switches`      | Physical switches, buttons, remotes and dimmers    |

Pick the category for what a blueprint mainly does, and keep the list short; a
blueprint can only live in one place.

Each blueprint folder holds the blueprint YAML, a `README.md`, and any images it uses.
Forked blueprints also carry an `UPSTREAM.md` recording where they came from, their
license, and the upstream commit they were last synced to.

A blueprint's path is part of its import URL (`source_url`), so once a blueprint is
published its folder should not move or be renamed.

## Adding a blueprint

1. Create `blueprints/<domain>/<category>/<name>/` and put `<name>.yaml` in it.
2. Set `source_url` to
   `https://raw.githubusercontent.com/AlexHallberg/Home-Assistant-Blueprints/main/blueprints/<domain>/<category>/<name>/<name>.yaml`.
3. Add a `README.md`, and an `UPSTREAM.md` if it is a fork.
4. Add a row to the table above.

## License

Blueprints written in this repository are under the [MIT license](LICENSE).
Forked blueprints keep their original license; see each one's `UPSTREAM.md`.
