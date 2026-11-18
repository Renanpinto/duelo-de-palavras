#!/usr/bin/env python3
"""Filter a FrequencyWords pt_BR list for the game's accepted guesses."""

from pathlib import Path
import re
import sys
import unicodedata


if len(sys.argv) != 5:
    raise SystemExit(
        "Uso: python3 tools/filter-word-list.py "
        "caminho/pt_br_50k.txt caminho/lexico caminho/conjugacoes caminho/verbos"
    )

source = Path(sys.argv[1])
lexicon_source = Path(sys.argv[2])
conjugations_source = Path(sys.argv[3])
verbs_source = Path(sys.argv[4])
destination = Path(__file__).resolve().parents[1] / "data/palavras-pt-br.txt"
allowed = re.compile(r"^[a-záàâãéêíóôõúüç]+$", re.IGNORECASE)

def normalize(word):
    return "".join(
        character
        for character in unicodedata.normalize("NFD", word.lower())
        if unicodedata.category(character) != "Mn"
    )


source_words = {
    normalize(word.strip())
    for word in lexicon_source.read_text(encoding="utf-8").splitlines()
    if allowed.fullmatch(word.strip())
}
words = []


def source_token(line):
    parts = line.split()
    return parts[0] if parts else ""


infinitives = {
    normalize(word)
    for word in verbs_source.read_text(encoding="utf-8").splitlines()
    if allowed.fullmatch(word.strip())
}
conjugated_forms = {
    normalize(word)
    for word in conjugations_source.read_text(encoding="utf-8").splitlines()
    if allowed.fullmatch(word.strip())
} - infinitives

# Homographs with common non-verbal uses stay in the word game. The upstream
# conjugation list does not include part-of-speech tags, so these are explicit.
nonverbal_homographs = {
    "acordo", "anda", "antes", "apenas", "casa", "canto", "como",
    "conta", "corte", "depois", "esta", "este", "fala", "gosto",
    "jogo", "mais", "marca", "menos", "nota", "passo", "parte",
    "porta", "ponto", "venda",
}


def likely_singulars(word):
    candidates = set()
    if word.endswith("oes"):
        candidates.add(word[:-3] + "ao")
    if word.endswith("aes"):
        candidates.update((word[:-3] + "ao", word[:-1]))
    if word.endswith("aos"):
        candidates.add(word[:-3] + "ao")
    for plural, singulars in {
        "ais": ("al",),
        "eis": ("el", "il"),
        "ois": ("ol",),
        "uis": ("ul",),
    }.items():
        if word.endswith(plural):
            candidates.update(word[:-len(plural)] + ending for ending in singulars)
    if word.endswith("ns"):
        candidates.add(word[:-2] + "m")
    if word.endswith("es"):
        candidates.add(word[:-2])
    if word.endswith("s"):
        candidates.add(word[:-1])
    return candidates


seen = set()
removed_conjugated = 0
removed_plural = 0
for line in source.read_text(encoding="utf-8").splitlines():
    token = source_token(line)
    if not allowed.fullmatch(token):
        continue
    normalized = normalize(token)
    if normalized not in source_words:
        continue
    if not 4 <= len(normalized) <= 7 or not normalized.isalpha():
        continue
    if normalized in conjugated_forms and normalized not in nonverbal_homographs:
        removed_conjugated += 1
        continue
    if (
        normalized not in nonverbal_homographs
        and any(candidate in source_words for candidate in likely_singulars(normalized))
    ):
        removed_plural += 1
        continue
    if normalized in seen:
        continue

    seen.add(normalized)
    words.append(normalized.upper())

destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text("\n".join(words) + "\n", encoding="utf-8")
print(
    f"{len(words)} palavras gravadas; {removed_conjugated} formas verbais e "
    f"{removed_plural} possíveis plurais removidos; "
    f"{destination.stat().st_size} bytes em {destination}"
)
