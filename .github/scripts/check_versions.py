"""Check that every blueprint carries a consistent calendar version.

For each blueprints/<domain>/<category>/<name>/<name>.yaml:
- the blueprint `name` ends with a version `vYYYY.M.N`,
- the same version appears again in the file (the description),
- the folder has a CHANGELOG.md with a `## vYYYY.M.N` heading for it.

Exits non-zero and prints one line per problem. See "Versioning" in the root README.
"""
import pathlib
import re
import sys

NAME = re.compile(r"^  name: .*\s(v\d{4}\.\d{1,2}\.\d+)\s*$", re.MULTILINE)

problems = []
blueprints = sorted(pathlib.Path("blueprints").glob("*/*/*/*.yaml"))
for path in blueprints:
    text = path.read_text(encoding="utf-8")
    match = NAME.search(text)
    if not match:
        problems.append(f"{path}: blueprint name does not end with a version like v2026.10.0")
        continue
    version = match.group(1)
    if text.count(version) < 2:
        problems.append(f"{path}: {version} is in the name but not in the description")
    changelog = path.parent / "CHANGELOG.md"
    if not changelog.exists():
        problems.append(f"{path}: missing {changelog}")
    elif not re.search(rf"^## {re.escape(version)}\b", changelog.read_text(encoding="utf-8"), re.MULTILINE):
        problems.append(f"{changelog}: no '## {version}' heading")

for problem in problems:
    print(problem)
print(f"Checked {len(blueprints)} blueprints, {len(problems)} problems")
sys.exit(1 if problems else 0)
