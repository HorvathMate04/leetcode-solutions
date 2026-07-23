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

# --- Konfiguracio ---------------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")

DIFFICULTY_FOLDERS = {
    "easy": {"label": "🟢 Easy", "plain": "Easy"},
    "medium": {"label": "🟡 Medium", "plain": "Medium"},
    "hard": {"label": "🔴 Hard", "plain": "Hard"},
}

FILENAME_PATTERN = re.compile(r"^(\d+)_(.+)\.py$")

# Csak a stats es progress szekciokat kezeli a script.
# Ha kesobb ujra kell a "Latest solved" vagy a teljes problemalista,
# eleg visszatenni a megfelelo marker-part a README.md-be, es egy
# build_xxx_section fuggvenyt + MARKERS bejegyzest hozza adni.
MARKERS = {
    "stats": ("<!-- START_STATS -->", "<!-- END_STATS -->"),
    "progress": ("<!-- START_PROGRESS -->", "<!-- END_PROGRESS -->"),
}


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


# --- README frissites --------------------------------------------------------

def replace_between_markers(content, start_marker, end_marker, new_body):
    """Lecsereli a ket marker kozotti tartalmat. Ha a marker-par nincs
    jelen a README.md-ben (pl. a felhasznalo kivette azt a szekciot),
    csendben kihagyja - nem all le hibaval."""
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        flags=re.DOTALL,
    )
    if not pattern.search(content):
        print(f"Info: marker paros nem talalhato, szekcio kihagyva: {start_marker} / {end_marker}")
        return content
    replacement = f"{start_marker}\n{new_body}\n{end_marker}"
    return pattern.sub(replacement, content)


def main():
    solutions = collect_solutions()

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    sections = {
        "stats": build_stats_section(solutions),
        "progress": build_progress_section(solutions),
    }

    for key, body in sections.items():
        start_marker, end_marker = MARKERS[key]
        content = replace_between_markers(content, start_marker, end_marker, body)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README.md frissitve. Talalt megoldasok: {len(solutions)}")


if __name__ == "__main__":
    main()
