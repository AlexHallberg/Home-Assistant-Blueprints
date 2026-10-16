# Home Assistant Auto-update

> [!NOTE]
> This is a fork of [ha_auto_update_scheduled](https://github.com/edwardtfn/ha_auto_update_scheduled)
> by [Edward Firmo](https://github.com/edwardtfn). See [UPSTREAM.md](UPSTREAM.md) for details.

Installs Home Assistant updates automatically: Core, OS, Supervisor, add-ons, HACS, device firmware
and anything else that shows up as an `update` entity. It can back up first, install the updates one
by one, restart when an update needs it, and pick up where it left off after a restart.

Current version: **v2026.10.2**, based on upstream v2026.6.0. See [CHANGELOG.md](CHANGELOG.md).

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.][import-badge]][import]

[import-badge]: https://my.home-assistant.io/badges/blueprint_import.svg
[import]: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexHallberg%2FHome-Assistant-Blueprints%2Fmain%2Fblueprints%2Fautomation%2Fsystem%2Fauto_update_scheduled%2Fauto_update_scheduled.yaml

> [!WARNING]
> Auto-updating can break things. Make sure you have working backups, and read the
> [community discussion](https://community.home-assistant.io/t/how-to-keep-everything-automatically-up-to-date/288938)
> about the risks before you turn it on.

## What this fork adds

- **Named steps in traces.** Every condition and action has a name, so a trace shows *why* a run
  stopped ("Updates are not paused", "Backup confirmed by a new timestamp") instead of
  "If any of 5 conditions matches".
- **Install log.** An optional log file with what each run found and installed, backups, restarts
  and errors. See [Install log](#install-log).
- **A minimum patch version per update type.** For example, hold Core back until `x.y.2` while
  installing HACS and add-on updates straight away, in one automation.
- **Working resume after a restart.** Upstream's "Update process started" toggle check never
  matched, so resuming after a restart was not detected and backups could be skipped.

## How a run works

The automation starts when an update appears, when Home Assistant starts, when automations are
reloaded, on a new day, or when the schedule turns on. It then:

1. Checks that it may run: inside the schedule (or no schedule is set), on an allowed day of the
   month, and not paused.
2. Lists the pending updates, after the update modes, minimum patch versions, inclusions and
   exclusions.
3. Runs your pre-update actions, then makes a backup if one is due.
4. Installs general updates, then firmware, then Core, then OS, one at a time. Anything left over is
   installed together at the end.
5. Restarts Home Assistant if an update needs it and restarting is enabled.
6. Runs your post-update actions.

### Schedule

With a **schedule entity** set, new update runs only start while it is on. Leave it empty to install
updates whenever they are found. **Out of schedule entities** are always updated as soon as an update
appears, even outside the schedule.

### Resuming after a restart

Core and OS updates restart Home Assistant in the middle of a run. To continue afterwards, set the
**"Update process started" toggle** to an `input_boolean` helper. The run turns it on at the start and
off at the end. When Home Assistant starts with the toggle on, the run resumes: it skips the
pre-update actions and the backup, since those already ran, and installs the rest.

A toggle left on for more than 6 hours, or found on by a run that was not started by a restart or
reload, is treated as left over from a run that did not finish. That run makes its backup as normal
and writes a note to the install log.

Use a separate toggle for each automation made from this blueprint.

## Install log

An optional plain-text log file. Runs with nothing to update write nothing.

```text
2026-10-16 18:08:07 [Auto Update Home Assistant] Found 2 updates:
  - ESPHome: 2026.9.3 -> 2026.10.0
  - Mushroom: 4.5.0 -> 4.6.0
2026-10-16 18:09:12 [Auto Update Home Assistant] Backup completed
2026-10-16 18:09:13 [Auto Update Home Assistant] Installing ESPHome: 2026.9.3 -> 2026.10.0
2026-10-16 18:11:40 [Auto Update Home Assistant] Installed ESPHome: 2026.9.3 -> 2026.10.0
2026-10-16 18:11:41 [Auto Update Home Assistant] Installing Mushroom: 4.5.0 -> 4.6.0
2026-10-16 18:31:41 [Auto Update Home Assistant] ERROR: Mushroom 4.5.0 -> 4.6.0 did not finish within 1200 seconds (installed version is now 4.5.0)
2026-10-16 18:31:45 [Auto Update Home Assistant] ERROR: 1 update not installed:
  - Mushroom: 4.5.0 -> 4.6.0
2026-10-16 18:31:45 [Auto Update Home Assistant] Finished: 1 of 2 updates installed
```

Errors and warnings can also be copied to a separate error log file.

Setup:

1. Allow Home Assistant to write files in the config folder by adding this to `configuration.yaml`,
   then restart:

   ```yaml
   homeassistant:
     allowlist_external_dirs:
       - /config
   ```

   This lets file-based integrations read and write anything in `/config`. To keep it narrower, allow
   a subfolder such as `/config/logs` instead and put the log files there.

2. Add the **File** integration under *Settings > Devices & Services*, choose
   **Set up a notification service**, and enter a path such as `/config/auto_update.log`.
   Leave **Timestamp** off; the blueprint writes its own. Repeat for an error log if you want one.

3. In the automation, open **Install log (optional)** and select the file notify entities.

A run that ends in a restart (for example a Core update) stops before the summary line; the last
entry is then the `Installing ...` line for the update that restarted Home Assistant.

## Inputs

All inputs are optional.

### When

| Input | What it does |
| ----- | ------------ |
| Schedule entity | Runs only start while this schedule is on. Leave empty to update whenever updates are found. |
| Earliest / latest day in the month | Only run between these days. `0` turns the check off. |
| Out of schedule entities | Update entities installed as soon as an update appears, even outside the schedule. |
| Pause update entities | While any of these is on, nothing is updated. |

### What

| Input | What it does |
| ----- | ------------ |
| Update mode (core and OS, firmware, general) | **All**, **Patches only** (`x.y.0` to `x.y.3`, not `x.y` to `x.y+1`) or **Don't update**. |
| Minimum patch version (core and OS, firmware, general) | Skip an update until its patch number reaches this value. `2` skips `x.y.0` and `x.y.1`. `0` turns it off. |
| Entity inclusion mode, list and searchfilter | Limit general updates to listed entities, or to entity IDs matching a filter such as `update.esphome_`. |
| Exclusions | Update entities that are never installed. |

"General" means everything that is not Core, OS, Supervisor or device firmware: add-ons, HACS,
integrations and so on. Supervisor follows the core and OS settings.

### Backup

| Input | What it does |
| ----- | ------------ |
| Create a backup before starting the updates? | **Never**, **Always**, or **When no recent backup is detected**. Uses your automatic backup settings. |
| Backup state sensor | `sensor.backup_backup_manager_state`. Used to wait for a running backup and to confirm the new one. |
| Last successful automatic backup sensor | `sensor.backup_last_successful_automatic_backup`. Needed for the "no recent backup" mode. |
| Maximum backup age | How old the last backup may be before a new one is made. Default 1 day. |
| Backup timeout | How long to wait for a backup to finish, in minutes. |

### Actions

| Input | What it does |
| ----- | ------------ |
| Pre-update actions | Run before the backup and updates. Not run again when resuming after a restart. |
| Pre-restart actions | Run before a restart that is skipped because the configuration check failed. |
| Post-update actions | Run after the updates. A run that ends in a restart does not get here. |
| Step actions | Run at each step: starting, backup, update progress, errors, restart, done. |

The variables `updates_list` (updates found when the run started) and `updates_pending` (updates
still to install) are available in these actions.

### Notifications

Send a message to a notify entity at the steps you pick: starting, backup, update progress, errors,
restart and done. Messages are plain text. For a log file, use the [install log](#install-log)
instead.

### General settings

| Input | What it does |
| ----- | ------------ |
| Force Home Assistant to restart if required by any update? | Restart Core or the host after updates that need a manual restart (common with HACS). |
| Log addon progress with verbosity to the logbook? | Write every step to the logbook. |
| "Update Process Started" toggle entity | Lets a run resume after a restart. See [Resuming after a restart](#resuming-after-a-restart). |
| Update timeout | How long to wait for each update before moving on. Default 1200 seconds. |

## Things to know

- **Supervisor** updates itself on Home Assistant OS, so it may update outside this automation.
- **Add-ons** with "Auto update" turned on in their own settings are updated by Home Assistant itself,
  not by this automation.
- **Restart detection** recognises HACS's "restart required" notice. Other updates that need a restart
  are not detected.
