"""Post two thematically related poetry lines, drawn from up to two different
poems, to a Discord channel via webhook.

Themes are inferred from shared significant words between poems (no LLM
call needed) so pairing stays coherent without any external API.
"""
import json
import os
import random
import re
from pathlib import Path

import requests

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "poems.json"

STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "your", "you", "not", "but",
    "are", "was", "were", "have", "has", "had", "all", "one", "when", "what",
    "who", "how", "why", "into", "onto", "off", "out", "over", "under", "than",
    "then", "them", "they", "their", "its", "his", "her", "him", "she", "he",
    "will", "would", "could", "should", "can", "did", "does", "just", "only",
    "own", "same", "such", "too", "very", "there", "here", "where", "while",
    "each", "some", "more", "most", "other", "again", "once", "still", "yet",
    "from", "these", "those", "which", "till", "until",
}

WORD_RE = re.compile(r"[a-zA-Z']+")


def significant_words(text: str) -> set:
    words = WORD_RE.findall(text.lower())
    return {w for w in words if len(w) > 3 and w not in STOPWORDS}


def load_poems():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        poems = json.load(f)
    for p in poems:
        p["wordset"] = significant_words(p["title"] + " " + " ".join(p["lines"]))
    return poems


def pick_thematic_pair(poems):
    poem_a = random.choice(poems)
    others = [p for p in poems if p is not poem_a]

    scored = []
    for p in others:
        overlap = poem_a["wordset"] & p["wordset"]
        if overlap:
            scored.append((len(overlap), p))

    if scored:
        scored.sort(key=lambda t: t[0], reverse=True)
        top_score = scored[0][0]
        best = [p for score, p in scored if score == top_score]
        poem_b = random.choice(best)
    else:
        poem_b = random.choice(others)

    return poem_a, poem_b


def main():
    poems = load_poems()
    poem_a, poem_b = pick_thematic_pair(poems)

    line_a = random.choice(poem_a["lines"]).rstrip(",")
    line_b = random.choice(poem_b["lines"]).rstrip(",")

    message = f"{line_a}\n{line_b}"
    print(f"From '{poem_a['title']}' + '{poem_b['title']}':\n{message}")

    webhook_url = os.environ["DISCORD_FIJI_BOT"]
    response = requests.post(webhook_url, json={"content": message})
    print("Status code:", response.status_code)
    print("Response body:", response.text)
    response.raise_for_status()


if __name__ == "__main__":
    main()
