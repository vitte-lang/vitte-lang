#!/usr/bin/env python3
import argparse
import json
import os
import re
import urllib.request
from pathlib import Path


def gh_get(url, token):
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_public_repos(org, token):
    page = 1
    repos = []
    while True:
        url = (
            f"https://api.github.com/orgs/{org}/repos"
            f"?per_page=100&page={page}&type=public"
        )
        data = gh_get(url, token)
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return repos


def parse_prefixes(values):
    prefixes = []
    for raw in values or []:
        for part in raw.split(","):
            part = part.strip().lower()
            if part:
                prefixes.append(part)
    return prefixes


def should_skip_repo(repo, exclude_archived, exclude_forks, exclude_prefixes):
    if exclude_archived and repo.get("archived"):
        return True
    if exclude_forks and repo.get("fork"):
        return True
    name = (repo.get("name") or "").lower()
    return any(name.startswith(prefix) for prefix in exclude_prefixes)


def load_rules(path):
    if not path:
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    rules = data.get("rules", [])
    return rules if isinstance(rules, list) else []


def rule_matches(rule, name, full_name):
    name_lower = name.lower()
    full_lower = full_name.lower()
    prefix = rule.get("name_prefix")
    if prefix and name_lower.startswith(prefix.lower()):
        return True
    contains = rule.get("name_contains")
    if contains and contains.lower() in name_lower:
        return True
    regex = rule.get("name_regex")
    if regex and re.search(regex, name, re.IGNORECASE):
        return True
    repo_prefix = rule.get("repo_prefix")
    if repo_prefix and full_lower.startswith(repo_prefix.lower()):
        return True
    repo_regex = rule.get("repo_regex")
    if repo_regex and re.search(repo_regex, full_name, re.IGNORECASE):
        return True
    return False


def apply_rules(entry, rules, name, full_name):
    for rule in rules:
        if not isinstance(rule, dict):
            continue
        if not rule_matches(rule, name, full_name):
            continue
        for key in ("logo", "color", "logoColor"):
            if key in rule:
                entry[key] = rule[key]
        if rule.get("stop", True):
            break


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


def default_project_entry(repo_name, full_name, rules):
    entry = {
        "name": repo_name,
        "repo": full_name,
        "logo": "github",
        "color": "2DA44E",
    }
    lower = repo_name.lower()
    if "vscode" in lower:
        entry["logo"] = "visualstudiocode"
        entry["color"] = "2F80ED"
    if "homebrew" in lower:
        entry["logo"] = "homebrew"
        entry["color"] = "F4A261"
    apply_rules(entry, rules, repo_name, full_name)
    return entry


def write_projects(path: Path, projects):
    lines = ["# Public projects (ordered)"]
    for project in projects:
        lines.append(f"- {project['name']}")
        lines.append(f"  repo: {project['repo']}")
        lines.append(f"  logo: {project.get('logo', 'github')}")
        lines.append(f"  color: {project.get('color', '2DA44E')}")
        logo_color = project.get("logoColor")
        if logo_color:
            lines.append(f"  logoColor: {logo_color}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("org")
    parser.add_argument("projects_path")
    parser.add_argument(
        "--exclude-archived",
        action="store_true",
        help="Ignore archived repositories.",
    )
    parser.add_argument(
        "--exclude-forks",
        action="store_true",
        help="Ignore forked repositories.",
    )
    parser.add_argument(
        "--exclude-prefix",
        action="append",
        default=[],
        help="Ignore repositories with these name prefixes (repeatable or comma list).",
    )
    parser.add_argument(
        "--rules",
        default="",
        help="Path to JSON rules for logo/color overrides.",
    )
    args = parser.parse_args()

    projects_path = Path(args.projects_path)
    existing = parse_projects(projects_path)
    by_repo = {p["repo"].lower(): p for p in existing if "repo" in p}

    token = os.environ.get("GITHUB_TOKEN", "")
    repos = fetch_public_repos(args.org, token)
    exclude_prefixes = parse_prefixes(args.exclude_prefix)
    rules = load_rules(args.rules)
    public_repos = sorted(
        {
            r["full_name"]
            for r in repos
            if r.get("full_name")
            and not should_skip_repo(
                r,
                args.exclude_archived,
                args.exclude_forks,
                exclude_prefixes,
            )
        },
        key=lambda x: x.lower(),
    )

    new_entries = []
    for full_name in public_repos:
        if full_name.lower() in by_repo:
            continue
        repo_name = full_name.split("/", 1)[1]
        new_entries.append(default_project_entry(repo_name, full_name, rules))

    updated = existing + new_entries
    write_projects(projects_path, updated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
