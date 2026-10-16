# Ideas

Things considered but not built yet.

## Auto-import new blueprints with Spook

Import blueprints added to this repo into Home Assistant automatically, so only updates need
[Spook's update entities](https://spook.boo/blueprint/).

**Design:**

- **`rest_command`** (YAML, in `configuration.yaml` or a package), both `GET`:
  - the GitHub API file list: `https://api.github.com/repos/AlexHallberg/Home-Assistant-Blueprints/git/trees/main?recursive=1`;
  - the raw text of one blueprint file, URL passed in as a variable.
- **Automation, once a day:**
  1. Get the file list and keep `blueprints/automation/**.yaml` and `blueprints/script/**.yaml`.
  2. Fetch each file and read its `name:`.
  3. Skip any blueprint that already has a Spook update entity whose title is that name.
  4. Call `blueprint.import` with the raw URL for the rest. It saves to `AlexHallberg/<file>.yaml`,
     the same path as the UI import button.
  5. Create a notification only when something was imported.
- **Location:** `ha-config/packages/blueprint_auto_import.yaml` in this repo.

**Why it skips instead of importing everything:**

- Spook's `blueprint.import` raises an error when the file already exists; it never overwrites.
- Home Assistant logs that at ERROR level even with `continue_on_error`.
- Importing everything every day would therefore log one error per existing blueprint.

**Things to know:**

- Spook's update entity does not expose the source URL, so the match is by blueprint name.
  Renaming a blueprint makes it look new until the Spook update with the new name is installed;
  until then the daily import fails with an error.
- Covers this repo only. Updates stay manual, through Spook.
- Needs testing on a live instance.
