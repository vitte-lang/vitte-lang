#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


def parse_projects(path: Path):
    projects = []
    current = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            if current:
                projects.append(current)
            current = {"name": line[2:].strip()}
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            current[key.strip()] = value.strip().strip('"').strip("'")
    if current:
        projects.append(current)
    return projects


def badge_line(project):
    label = project["name"]
    repo = project["repo"]
    color = project.get("color", "2DA44E")
    logo = project.get("logo", "github")
    logo_color = project.get("logoColor", "white")
    return (
        f"[![{label}]"
        f"(https://img.shields.io/badge?label={label}"
        f"&message=public&color={color}&style=for-the-badge"
        f"&logo={logo}&logoColor={logo_color})]"
        f"(https://github.com/{repo})"
    )


def render_block(projects):
    lines = [badge_line(p) for p in projects]
    return "\n".join(lines)


def replace_block(readme_text, block):
    pattern = re.compile(
        r"<!-- PROJECT_BADGES_START -->.*?<!-- PROJECT_BADGES_END -->",
        re.DOTALL,
    )
    replacement = f"<!-- PROJECT_BADGES_START -->\n{block}\n<!-- PROJECT_BADGES_END -->"
    if not pattern.search(readme_text):
        raise SystemExit("Marker block not found in README.md")
    return pattern.sub(replacement, readme_text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("projects_path")
    parser.add_argument("readme_path")
    args = parser.parse_args()

    projects = parse_projects(Path(args.projects_path))
    block = render_block(projects)
    readme_path = Path(args.readme_path)
    updated = replace_block(readme_path.read_text(encoding="utf-8"), block)
    readme_path.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
