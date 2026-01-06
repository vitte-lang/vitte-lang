#!/usr/bin/env python3
import argparse
import json
import os
import re
import urllib.request

IGNORED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "out",
    "target",
}
PINNED_LANGS = ["Vitte", "Muffin"]


def gh_get(url, token):
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8")), resp.headers


def sanitize_name(name):
    safe = re.sub(r"[^a-z0-9_-]+", "_", name.lower())
    return safe.strip("_") or "lang"


def lang_color(name):
    key = name.strip().lower()
    if key == "vitte":
        return "6E56CF"
    if key == "muffin":
        return "FFB703"
    return "blue"


def write_badge(path, label, message, color):
    payload = {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "color": color,
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f)
        f.write("\n")


def normalize_lang_name(name):
    key = name.strip().lower()
    if key in {".vit", ".vitte", "vit", "vitte"}:
        return "Vitte"
    if key in {"muffin", ".muf", ".muffin"}:
        return "Muffin"
    return name.strip()


def parse_manual(raw):
    items = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(f"invalid manual entry: {part}")
        name, value = part.split("=", 1)
        name = normalize_lang_name(name)
        value = value.strip().replace(",", ".")
        percent = float(value)
        items.append((name, percent))
    return items


def detect_custom_language(path):
    name = os.path.basename(path)
    lower = name.lower()
    if lower in {"muffin", "muffinfile"}:
        return "Muffin"
    _root, ext = os.path.splitext(lower)
    if ext in {".vit", ".vitte"}:
        return "Vitte"
    if ext in {".muf", ".muffin"}:
        return "Muffin"
    return None


def scan_custom_languages(root_path):
    totals = {"Vitte": 0, "Muffin": 0}
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for name in files:
            path = os.path.join(root, name)
            if not os.path.isfile(path):
                continue
            lang = detect_custom_language(path)
            if not lang:
                continue
            try:
                size = os.path.getsize(path)
            except OSError:
                continue
            totals[lang] += size
    return {lang: size for lang, size in totals.items() if size > 0}


def build_summary(data, total, top, pinned):
    if total <= 0:
        return "no data"
    ordered = sorted(data.items(), key=lambda x: x[1], reverse=True)
    summary_langs = ordered[:top]
    present = {lang for lang, _size in summary_langs}
    for lang in pinned:
        if data.get(lang, 0) > 0 and lang not in present:
            summary_langs.append((lang, data[lang]))
            present.add(lang)
    parts = [f"{lang} {(size / total) * 100:.1f}%" for lang, size in summary_langs]
    return " | ".join(parts) if parts else "no data"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("owner")
    parser.add_argument("repo")
    parser.add_argument("output_dir")
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument(
        "--langs",
        default="Vitte,Muffin",
        help="Comma list of languages to emit per-language badges for.",
    )
    parser.add_argument(
        "--scan-path",
        default=".",
        help="Path to scan for custom languages (Vitte/Muffin).",
    )
    parser.add_argument(
        "--no-scan",
        action="store_true",
        help="Disable local scan for custom languages.",
    )
    parser.add_argument(
        "--manual",
        default="",
        help="Manual list like 'Perl=50,Vitte=30,Muffin=0.5' (overrides GitHub data).",
    )
    args = parser.parse_args()

    if args.manual:
        manual_items = parse_manual(args.manual)
        parts = [f"{name} {percent:.1f}%" for name, percent in manual_items]
        summary_message = " | ".join(parts) if parts else "no data"
        manual_map = {name: percent for name, percent in manual_items}
        total = 100.0
        data = {}
    else:
        token = os.environ.get("GITHUB_TOKEN", "")
        url = f"https://api.github.com/repos/{args.owner}/{args.repo}/languages"
        data, _headers = gh_get(url, token)

        if not args.no_scan:
            custom = scan_custom_languages(args.scan_path)
            for lang, size in custom.items():
                if lang not in data:
                    data[lang] = size

        total = sum(data.values())
        summary_message = build_summary(data, total, args.top, PINNED_LANGS)
        manual_map = {}

    summary_path = os.path.join(args.output_dir, "languages_summary.json")
    write_badge(summary_path, "Languages", summary_message, "blue")

    requested = [normalize_lang_name(l) for l in args.langs.split(",") if l.strip()]
    for lang in requested:
        if args.manual:
            percent = manual_map.get(lang, 0.0)
        else:
            size = data.get(lang, 0)
            percent = (size / total) * 100 if total > 0 else 0.0
        message = f"{percent:.1f}%"
        label = f"{lang} %"
        filename = f"lang_{sanitize_name(lang)}.json"
        path = os.path.join(args.output_dir, filename)
        write_badge(path, label, message, lang_color(lang))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
