#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry (@syukuran).

A deterministic program that writes a single-sentence, one-star review of
planet Earth by an alien field scientist to /output/entry.txt.

The reviewer is a xeno-anthropologist on a research trip: her field notes
record a species that fears its own weather, worships glowing rectangles
and eats with sticks — yet one bowl of gudeg forces her to rewrite her
whole thesis on intelligent life. That is the joke's turn: the food is the
only data point that survives peer review.

The review is assembled from fixed parts (no randomness, no network, no
input besides the program itself), so every run writes byte-identical
output. A gate check runs before any write: the text must be one
sentence, a single line, and within the 1–200 character gate.
"""

import sys
from pathlib import Path

# --- The field report -------------------------------------------------------
# Voice: a xeno-anthropologist filing her Earth report. Her observations
# are clinical (field notes, dominant species, thesis) and her grievances
# are an outsider's bafflement at human habits; her praise is clinical too
# — the gudeg is the one finding that overturns her conclusions.

RATING = "One star:"
FIELD_NOTES = (
    "my field notes record a species that fears its own weather, "
    "worships glowing rectangles, and eats with sticks"
)
FINDING = (
    "yet one bowl of gudeg forced me to rewrite "
    "my thesis on intelligent life"
)

MAX_CHARS = 200
DEFAULT_OUTPUT = Path("/output/entry.txt")


def compose_review() -> str:
    """Join the report's parts into the single review sentence."""
    return f"{RATING} {FIELD_NOTES} \u2014 {FINDING}."


def check_gate(text: str) -> list[str]:
    """Return every gate violation in the review (empty means it passes)."""
    problems = []
    if not text or text.isspace():
        problems.append("review is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        problems.append(f"review is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.count(".") != 1 or not text.endswith("."):
        problems.append("review must be exactly one sentence")
    if "\n" in text or "\r" in text:
        problems.append("review must be a single line")
    return problems


def self_check() -> int:
    """Print the review and its gate numbers; exit 0 only on a pass."""
    review = compose_review()
    problems = check_gate(review)
    print(f"review: {review}")
    print(f"characters: {len(review)} (limit {MAX_CHARS})")
    print(f"bytes: {len(review.encode('utf-8'))}")
    print(f"sentences: {review.count('.')}")
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1
    print("self-check: PASS")
    return 0


def main(argv: list[str]) -> int:
    if "--self-check" in argv:
        return self_check()
    out_path = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    review = compose_review()
    problems = check_gate(review)
    if problems:
        raise ValueError("; ".join(problems))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(review + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
