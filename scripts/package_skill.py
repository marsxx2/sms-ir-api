#!/usr/bin/env python3
"""
Package a Claude Skill folder into a distributable .skill file.

A .skill file is just a zip archive of the skill's folder (kept under its
own top-level folder name inside the zip), with a couple of build-artifact
patterns excluded. This script has no dependencies beyond the Python
standard library.

Usage:
    python3 scripts/package_skill.py <path/to/skill-folder> [output-directory]

Example:
    python3 scripts/package_skill.py skill/sms-ir-api
    python3 scripts/package_skill.py skill/sms-ir-api ./dist
"""

import fnmatch
import sys
import zipfile
from pathlib import Path

EXCLUDE_DIRS = {"__pycache__", "node_modules", ".git"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_FILES = {".DS_Store"}


def should_exclude(rel_path: Path) -> bool:
    parts = rel_path.parts
    if any(part in EXCLUDE_DIRS for part in parts):
        return True
    if rel_path.name in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(rel_path.name, pat) for pat in EXCLUDE_GLOBS)


def package_skill(skill_path: str, output_dir: str | None = None) -> Path | None:
    skill_path = Path(skill_path).resolve()

    if not skill_path.is_dir():
        print(f"Error: not a directory: {skill_path}")
        return None

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"Error: SKILL.md not found in {skill_path}")
        return None

    output_path = Path(output_dir).resolve() if output_dir else Path.cwd()
    output_path.mkdir(parents=True, exist_ok=True)

    skill_filename = output_path / f"{skill_path.name}.skill"

    with zipfile.ZipFile(skill_filename, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_path.rglob("*"):
            if not file_path.is_file():
                continue
            arcname = file_path.relative_to(skill_path.parent)
            if should_exclude(arcname):
                print(f"  skipped: {arcname}")
                continue
            zf.write(file_path, arcname)
            print(f"  added:   {arcname}")

    print(f"\nDone: {skill_filename}")
    return skill_filename


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    result = package_skill(skill_path, output_dir)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
