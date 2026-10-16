# Home Assistant Blueprints

A collection of Home Assistant blueprints: some written here, some forked from other
authors with local changes.

## Blueprints

| Blueprint | Type | Origin | Import |
| --------- | ---- | ------ | ------ |
| [Auto-update on a schedule](blueprints/automation/auto_update_scheduled/) | Automation | Fork of [edwardtfn][upstream-auto-update] | [![Import][import-badge]][import-auto-update] |

[import-badge]: https://my.home-assistant.io/badges/blueprint_import.svg
[upstream-auto-update]: https://github.com/edwardtfn/ha_auto_update_scheduled
[import-auto-update]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Fauto_update_scheduled%2Fauto_update_scheduled.yaml

## Repository layout

```text
blueprints/
  automation/<name>/   automation blueprints
  script/<name>/       script blueprints
  template/<name>/     template blueprints
```

Each blueprint folder holds the blueprint YAML, a `README.md`, and any images it uses.
Forked blueprints also carry an `UPSTREAM.md` recording where they came from, their
license, and the upstream commit they were last synced to.

A blueprint's path is part of its import URL (`source_url`), so once a blueprint is
published its folder should not move or be renamed.

## Adding a blueprint

1. Create `blueprints/<domain>/<name>/` and put `<name>.yaml` in it.
2. Set `source_url` to
   `https://raw.githubusercontent.com/AlexHallberg/Home-Assistant-Blueprints/main/blueprints/<domain>/<name>/<name>.yaml`.
3. Add a `README.md`, and an `UPSTREAM.md` if it is a fork.
4. Add a row to the table above.

## License

Blueprints written in this repository are under the [MIT license](LICENSE).
Forked blueprints keep their original license; see each one's `UPSTREAM.md`.
