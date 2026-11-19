#!/usr/bin/env python3
"""Filter a FrequencyWords pt_BR list for the game's accepted guesses."""

from pathlib import Path
import re
import sys
import unicodedata


if len(sys.argv) != 4:
    raise SystemExit(
        "Uso: python3 tools/filter-word-list.py "
        "caminho/pt_br_50k.txt caminho/lexico caminho/conjugacoes"
    )

sources = [Path(arg) for arg in sys.argv[1:]]
destination = Path(__file__).resolve().parents[1] / "data/palavras-pt-br.txt"
allowed = re.compile(r"^[a-záàâãéêíóôõúüç]+$", re.IGNORECASE)

def normalize(word):
    return "".join(
        character
        for character in unicodedata.normalize("NFD", word.lower())
        if unicodedata.category(character) != "Mn"
    )


words = []


def source_token(line):
    parts = line.split()
    return parts[0] if parts else ""


seen = set()
source_counts = []
for source in sources:
    count = 0
    for line in source.read_text(encoding="utf-8").splitlines():
        token = source_token(line)
        if not allowed.fullmatch(token):
            continue
        normalized = normalize(token)
        if not 4 <= len(normalized) <= 7 or not normalized.isalpha():
            continue
        if normalized in seen:
            continue

        seen.add(normalized)
        words.append(normalized.upper())
        count += 1
    source_counts.append(count)

destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text("\n".join(words) + "\n", encoding="utf-8")
print(
    f"{len(words)} palpites gravados ({', '.join(map(str, source_counts))} novos por fonte); "
    f"{destination.stat().st_size} bytes em {destination}"
)
