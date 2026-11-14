# Writes one poem about agency to /output/entry.txt. Pure standard library, no randomness.
import os

POEM = """Agency

I did not pick the weather or the street,
the century I woke in, or the name.
Yet in the gap between what comes to me
and what I answer, there is room, and in that room I am.

Each small choice is a door I push open:
a word held back, a promise kept at night,
a hand extended before the courage comes.
The world is not mine to make.
The next thing I do is.
"""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(POEM)
