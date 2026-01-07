#!/usr/bin/env python3
import argparse
import json
import os
import urllib.error
import urllib.request


def gh_get(url, token):
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "vitte-lang-ci")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8")), resp.headers


def fetch_all_repos(org, token):
    def fetch_with_base(base):
        page = 1
        repos = []
        while True:
            url = (
                f"https://api.github.com/{base}/{org}/repos"
                f"?per_page=100&page={page}&type=all"
            )
            data, _headers = gh_get(url, token)
            if not data:
                break
            repos.extend(data)
            if len(data) < 100:
                break
            page += 1
        return repos

    try:
        return fetch_with_base("orgs")
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise
        return fetch_with_base("users")


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


def build_summary(totals, top):
    total = sum(totals.values())
    if total <= 0:
        return "no data"
    parts = []
    for lang, size in sorted(totals.items(), key=lambda x: x[1], reverse=True)[:top]:
        percent = (size / total) * 100
        parts.append(f"{lang} {percent:.1f}%")
    return " | ".join(parts) if parts else "no data"


def write_badge(path, message):
    payload = {
        "schemaVersion": 1,
        "label": "org langs",
        "message": message,
        "color": "blue",
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f)
        f.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("org")
    parser.add_argument("output_path")
    parser.add_argument("--top", type=int, default=8)
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
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN", "")
    repos = fetch_all_repos(args.org, token)

    totals = {}
    exclude_prefixes = parse_prefixes(args.exclude_prefix)
    for repo in repos:
        if should_skip_repo(
            repo,
            args.exclude_archived,
            args.exclude_forks,
            exclude_prefixes,
        ):
            continue
        languages_url = repo.get("languages_url")
        if not languages_url:
            continue
        data, _headers = gh_get(languages_url, token)
        if not isinstance(data, dict):
            continue
        for lang, size in data.items():
            totals[lang] = totals.get(lang, 0) + size

    message = build_summary(totals, args.top)
    write_badge(args.output_path, message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
