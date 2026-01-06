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


def fetch_repo(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    data, _headers = gh_get(url, token)
    return data


def main():
    if len(sys.argv) < 4:
        print("usage: update_repo_totals.py <owner> <repo> <output_path>")
        return 2

    owner = sys.argv[1]
    repo = sys.argv[2]
    out_path = sys.argv[3]
    token = os.environ.get("GITHUB_TOKEN", "")

    data = fetch_repo(owner, repo, token)
    stars = data.get("stargazers_count", 0)
    forks = data.get("forks_count", 0)
    issues = data.get("open_issues_count", 0)

    message = f"★{stars} | forks {forks} | issues {issues}"

    payload = {
        "schemaVersion": 1,
        "label": "repo total",
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
