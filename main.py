#!/usr/bin/env python3
"""Alien tourist's one-star review of Earth (with a food compliment).

Entry for make.fun's "One Star, Five Stars for the Food" bounty
(u-po-pu-one-star-five-stars-for-the-food-f9166ee7).

Writes exactly one sentence (<= 200 characters) to /output/entry.txt.
Deterministic: the same sentence, byte for byte, on every run.
"""

import os

# The review: one sentence, 169 characters. An alien tourist's genuine
# one-star grievance (paying to drink water, queuing, apologising to
# machines) with a real compliment about the food tucked into the turn.
ENTRY = (
    "Earth gets one star: its locals pay to drink water, queue for "
    "everything, and apologise to machines \u2014 but the dumplings almost "
    "made the forty-light-year flight worth it."
)


def main() -> None:
    # Guard the gate before writing: the scorer requires UTF-8 text of
    # 1-200 characters, not only whitespace, and exactly one sentence.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert sum(ENTRY.count(c) for c in ".!?") == 1, "entry must be one sentence"
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
