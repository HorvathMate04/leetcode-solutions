"""
update_readme.py

Bejarja az easy/, medium/, hard/ mappakat, kiszamolja a statisztikakat,
es a README.md megfelelo szekcioit (marker kommentek kozott) automatikusan
frissiti. Kizarolag Python standard library-t hasznal.

Futtatas:
    python scripts/update_readme.py

A script a repo gyokerebol felteteti magat futtatva (onnan hivja a
GitHub Actions workflow is).
"""

import os
import re
import subprocess
from datetime import datetime, timezone

# --- Konfiguracio ---------------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")

DIFFICULTY_FOLDERS = {
    "easy": {"label": "🟢 Easy", "plain": "Easy"},
    "medium": {"label": "🟡 Medium", "plain": "Medium"},
    "hard": {"label": "🔴 Hard", "plain": "Hard"},
}

FILENAME_PATTERN = re.compile(r"^(\d+)_(.+)\.py$")

MARKERS = {
    "stats": ("<!-- START_STATS -->", "<!-- END_STATS -->"),
    "progress": ("<!-- START_PROGRESS -->", "<!-- END_PROGRESS -->"),
    "latest": ("<!-- START_LATEST -->", "<!-- END_LATEST -->"),
    "problem_list": ("<!-- START_PROBLEM_LIST -->", "<!-- END_PROBLEM_LIST -->"),
}

LATEST_COUNT = 10  # hany legutobbi megoldast listazzunk ki


# --- Adatgyujtes -----------------------------------------------------------

def collect_solutions():
    """Bejarja a nehezsegi mappakat, es visszaadja a talalt megoldasok listajat."""
    solutions = []
    for folder, meta in DIFFICULTY_FOLDERS.items():
        folder_path = os.path.join(REPO_ROOT, folder)
        if not os.path.isdir(folder_path):
            continue
        for filename in os.listdir(folder_path):
            if not filename.endswith(".py"):
                continue
            match = FILENAME_PATTERN.match(filename)
            if not match:
                continue
            number, raw_name = match.groups()
            problem_name = raw_name.replace("_", " ").title()
            filepath = os.path.join(folder_path, filename)
            solutions.append(
                {
                    "number": number,
                    "name": problem_name,
                    "difficulty": folder,
                    "difficulty_label": meta["label"],
                    "filepath": filepath,
                    "rel_path": os.path.relpath(filepath, REPO_ROOT).replace(os.sep, "/"),
                }
            )
    solutions.sort(key=lambda s: s["number"])
    return solutions


def get_commit_date(filepath):
    """Visszaadja a fajl utolso git commit datumat (ISO), vagy a fajl mtime-jat,
    ha a git nem elerheto (pl. helyi tesztelesnel)."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", filepath],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        date_str = result.stdout.strip()
        if date_str:
            return datetime.fromisoformat(date_str)
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        pass
    return datetime.fromtimestamp(os.path.getmtime(filepath), tz=timezone.utc)


# --- Szekciok generalasa ----------------------------------------------------

def build_stats_section(solutions):
    counts = {folder: 0 for folder in DIFFICULTY_FOLDERS}
    for s in solutions:
        counts[s["difficulty"]] += 1
    total = sum(counts.values())

    lines = [
        "| Difficulty | Solved |",
        "|------------|--------|",
    ]
    for folder, meta in DIFFICULTY_FOLDERS.items():
        lines.append(f"| {meta['label']} | {counts[folder]} |")
    lines.append(f"| **Total** | **{total}** |")
    return "\n".join(lines)


def build_progress_section(solutions):
    counts = {folder: 0 for folder in DIFFICULTY_FOLDERS}
    for s in solutions:
        counts[s["difficulty"]] += 1
    total = sum(counts.values())

    if total == 0:
        return "_Meg nincs megoldott feladat._"

    lines = [f"**Összesen megoldott problémák: {total}**", ""]
    for folder, meta in DIFFICULTY_FOLDERS.items():
        pct = (counts[folder] / total) * 100
        filled = int(round(pct / 5))  # 20 karakteres sav
        bar = "█" * filled + "░" * (20 - filled)
        lines.append(f"- {meta['label']}: `{bar}` {pct:.1f}% ({counts[folder]})")
    return "\n".join(lines)


def build_latest_section(solutions):
    if not solutions:
        return "_Meg nincs megoldott feladat._"

    dated = [(get_commit_date(s["filepath"]), s) for s in solutions]
    dated.sort(key=lambda x: x[0], reverse=True)

    lines = [
        "| Date | # | Problem | Difficulty |",
        "|------|---|---------|------------|",
    ]
    for date, s in dated[:LATEST_COUNT]:
        lines.append(
            f"| {date.strftime('%Y-%m-%d')} | {s['number']} | "
            f"[{s['name']}]({s['rel_path']}) | {s['difficulty_label']} |"
        )
    return "\n".join(lines)


def build_problem_list_section(solutions):
    if not solutions:
        return "_Meg nincs megoldott feladat._"

    lines = [
        "| # | Problem | Difficulty |",
        "|---|---------|------------|",
    ]
    for s in solutions:
        lines.append(
            f"| {s['number']} | [{s['name']}]({s['rel_path']}) | {s['difficulty_label']} |"
        )
    return "\n".join(lines)


# --- README frissites --------------------------------------------------------

def replace_between_markers(content, start_marker, end_marker, new_body):
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        flags=re.DOTALL,
    )
    replacement = f"{start_marker}\n{new_body}\n{end_marker}"
    if not pattern.search(content):
        raise ValueError(f"Marker paros nem talalhato a README.md-ben: {start_marker} / {end_marker}")
    return pattern.sub(replacement, content)


def main():
    solutions = collect_solutions()

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    sections = {
        "stats": build_stats_section(solutions),
        "progress": build_progress_section(solutions),
        "latest": build_latest_section(solutions),
        "problem_list": build_problem_list_section(solutions),
    }

    for key, body in sections.items():
        start_marker, end_marker = MARKERS[key]
        content = replace_between_markers(content, start_marker, end_marker, body)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README.md frissitve. Talalt megoldasok: {len(solutions)}")


if __name__ == "__main__":
    main()
