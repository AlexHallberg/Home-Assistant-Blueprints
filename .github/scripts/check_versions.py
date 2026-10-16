"""Check that every blueprint carries a consistent calendar version.

For each blueprints/<domain>/<category>/<name>/<name>.yaml:
- the description has exactly one "Version vYYYY.M.N" line,
- the blueprint `name` does not contain a version (Spook's update entity takes its
  entity ID from the name, so a version there would stay frozen in the entity ID),
- the folder has a CHANGELOG.md with a `## vYYYY.M.N` heading for it.

Exits non-zero and prints one line per problem. See "Versioning" in the root README.
"""
import pathlib
import re
import sys

VERSION = r"v\d{4}\.\d{1,2}\.\d+"
MARKER = re.compile(rf"^    Version ({VERSION})\b", re.MULTILINE)
NAME = re.compile(r"^  name: (.*)$", re.MULTILINE)

problems = []
blueprints = sorted(pathlib.Path("blueprints").glob("*/*/*/*.yaml"))
for path in blueprints:
    text = path.read_text(encoding="utf-8")

    name = NAME.search(text)
    if name and re.search(VERSION, name.group(1)):
        problems.append(f"{path}: blueprint name contains a version; keep it in the description only")

    markers = MARKER.findall(text)
    if len(markers) != 1:
        problems.append(f"{path}: description needs exactly one 'Version vYYYY.M.N' line, found {len(markers)}")
        continue
    version = markers[0]

    changelog = path.parent / "CHANGELOG.md"
    if not changelog.exists():
        problems.append(f"{path}: missing {changelog}")
    elif not re.search(rf"^## {re.escape(version)}\b", changelog.read_text(encoding="utf-8"), re.MULTILINE):
        problems.append(f"{changelog}: no '## {version}' heading")

for problem in problems:
    print(problem)
print(f"Checked {len(blueprints)} blueprints, {len(problems)} problems")
sys.exit(1 if problems else 0)
