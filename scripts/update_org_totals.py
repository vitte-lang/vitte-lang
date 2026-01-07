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
                f"?per_page=100&page={page}"
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("org")
    parser.add_argument("output_path")
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

    org = args.org
    out_path = args.output_path
    token = os.environ.get("GITHUB_TOKEN", "")

    repos = fetch_all_repos(org, token)
    exclude_prefixes = parse_prefixes(args.exclude_prefix)
    filtered = [
        r
        for r in repos
        if not should_skip_repo(
            r,
            args.exclude_archived,
            args.exclude_forks,
            exclude_prefixes,
        )
    ]
    stars = sum(r.get("stargazers_count", 0) for r in filtered)
    forks = sum(r.get("forks_count", 0) for r in filtered)
    issues = sum(r.get("open_issues_count", 0) for r in filtered)

    message = f"★{stars} | forks {forks} | issues {issues}"

    payload = {
        "schemaVersion": 1,
        "label": "org total",
        "message": message,
        "color": "blue",
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f)
        f.write("\n")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
