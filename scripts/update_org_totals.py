#!/usr/bin/env python3
import json
import os
import sys
import urllib.request

def gh_get(url, token):
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8")), resp.headers

def fetch_all_repos(org, token):
    page = 1
    repos = []
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?per_page=100&page={page}"
        data, headers = gh_get(url, token)
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return repos

def main():
    if len(sys.argv) < 3:
        print("usage: update_org_totals.py <org> <output_path>")
        return 2

    org = sys.argv[1]
    out_path = sys.argv[2]
    token = os.environ.get("GITHUB_TOKEN", "")

    repos = fetch_all_repos(org, token)
    stars = sum(r.get("stargazers_count", 0) for r in repos)
    forks = sum(r.get("forks_count", 0) for r in repos)
    issues = sum(r.get("open_issues_count", 0) for r in repos)

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
