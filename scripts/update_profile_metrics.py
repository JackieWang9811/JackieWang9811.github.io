#!/usr/bin/env python3
"""Refresh public profile metrics for the homepage.

The site is static, so this script writes the latest successful values into
_data/profile_metrics.yml. If Scholar or CSDN blocks an automated request, the
previous value is kept instead of failing the build.
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "_data" / "profile_metrics.yml"
GITHUB_USER = "JackieWang9811"
GITHUB_EXTRA_REPOS = [
    "TheBrainLab/Awesome-Spiking-Neural-Networks",
    "TheBrainLab/npuslim",
]
SCHOLAR_ID = "jz4IkO0AAAAJ"
CSDN_USER = "jq_98"


def read_existing() -> dict[str, str]:
    if not DATA_FILE.exists():
        return {}

    metrics: dict[str, str] = {}
    for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        metrics[key.strip()] = value.strip().strip('"').strip("'")
    return metrics


def write_metrics(metrics: dict[str, str]) -> None:
    keys = [
        "google_scholar_citations",
        "github_stars",
        "csdn_views",
        "updated_at",
    ]
    lines = [f'{key}: "{metrics.get(key, "")}"' for key in keys]
    DATA_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_int(value: int | str) -> str:
    return f"{int(str(value).replace(',', '')):,}"


def fetch_text(url: str, headers: dict[str, str] | None = None) -> str:
    request_headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    }
    if headers:
        request_headers.update(headers)

    request = urllib.request.Request(url, headers=request_headers)
    with urllib.request.urlopen(request, timeout=25) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def keep_previous_on_error(name: str, previous: dict[str, str], fetcher) -> str:
    try:
        value = fetcher()
        if value:
            print(f"{name}: {value}")
            return value
    except Exception as exc:  # noqa: BLE001 - this is a best-effort updater.
        print(f"{name}: keeping previous value after {exc!r}", file=sys.stderr)
    return previous.get(name, "")


def fetch_github_stars() -> str:
    total = 0
    counted_repos: set[str] = set()
    page = 1
    while True:
        query = urllib.parse.urlencode(
            {"per_page": 100, "type": "owner", "sort": "full_name", "page": page}
        )
        url = f"https://api.github.com/users/{GITHUB_USER}/repos?{query}"
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "JackieWang9811.github.io metrics updater",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        with urllib.request.urlopen(request, timeout=25) as response:
            repos = json.loads(response.read().decode("utf-8"))
        if not repos:
            break
        for repo in repos:
            full_name = repo.get("full_name")
            if full_name and full_name not in counted_repos:
                counted_repos.add(full_name)
                total += int(repo.get("stargazers_count", 0))
        if len(repos) < 100:
            break
        page += 1

    for full_name in GITHUB_EXTRA_REPOS:
        if full_name in counted_repos:
            continue
        url = f"https://api.github.com/repos/{full_name}"
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "JackieWang9811.github.io metrics updater",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        with urllib.request.urlopen(request, timeout=25) as response:
            repo = json.loads(response.read().decode("utf-8"))
        counted_repos.add(full_name)
        total += int(repo.get("stargazers_count", 0))

    return format_int(total)


def fetch_google_scholar_citations() -> str:
    hosts = [
        "https://scholar.google.com",
        "https://scholar.google.com.hk",
        "https://scholar.google.com.ru",
    ]
    last_error: Exception | None = None
    for host in hosts:
        url = f"{host}/citations?hl=en&user={SCHOLAR_ID}"
        try:
            html = fetch_text(url)
            match = re.search(r'<td class="gsc_rsb_std">\s*([\d,]+)\s*</td>', html)
            if match:
                return format_int(match.group(1))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            time.sleep(2)
    if last_error:
        raise last_error
    raise RuntimeError("Google Scholar citation count was not found")


def fetch_csdn_views() -> str:
    url = f"https://blog.csdn.net/{CSDN_USER}"
    html = fetch_text(
        url,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "https://blog.csdn.net/",
        },
    )
    patterns = [
        r'<div class="user-profile-statistics-num"[^>]*>\s*([\d,]+)\s*</div>\s*'
        r'<div class="user-profile-statistics-name"[^>]*>\s*总访问量\s*</div>',
    ]
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return format_int(match.group(1))
    raise RuntimeError("CSDN total views were not found")


def main() -> None:
    previous = read_existing()
    metrics = dict(previous)
    metrics["github_stars"] = keep_previous_on_error(
        "github_stars", previous, fetch_github_stars
    )
    metrics["google_scholar_citations"] = keep_previous_on_error(
        "google_scholar_citations", previous, fetch_google_scholar_citations
    )
    metrics["csdn_views"] = keep_previous_on_error("csdn_views", previous, fetch_csdn_views)
    metrics["updated_at"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    write_metrics(metrics)


if __name__ == "__main__":
    main()
