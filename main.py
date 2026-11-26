# Worst Superpower — one-line entry (1-140 chars, written to /output/entry.txt)
#
# Judge criteria (RULES, in order):
#   1) genuinely useless superpower in one line (real/useful/merely-weak loses)
#   2) uselessness lands as a joke — reader pictures it in use, laughs at how little it achieves
#   3) unexpected, not a familiar gag (avoid slow flight, invisible-only-when-unwatched)
#   4) tight and specific, with a concrete detail
#   5) clear on a single reading
# A curse, or a power that quietly helps, is not a useless superpower.
#
# Candidate scoring (1-5 per criterion, in order above):
#
# Candidate A: "You can teleport exactly one inch to the left, but only while wearing a wet sock on your right foot."
#   1:3 (one inch could still dodge or slip a restraint — merely weak, not fully useless)
#   2:4 (wet-sock hero is a funny picture)  3:4 (fresh)  4:5 (one inch, right foot)  5:5  -> 21
#
# Candidate B: "You can summon a single paperclip, but only on Tuesdays in July, and it arrives slightly bent."
#   1:4 (a bent paperclip can still clip paper — quietly helps a little)
#   2:3 (mild picture)  3:4 (fresh)  4:5 (Tuesdays in July, slightly bent)  5:5  -> 21
#
# Candidate C: "You can instantly know the exact temperature of any soup you are already tasting."
#   1:5 (by the time you taste it the information can change nothing — achieves nothing new)
#   2:5 (hero sips soup and proudly announces a number nobody needs)
#   3:5 (no familiar gag)  4:4 (soup + exact temperature; unit would tighten it)  5:5  -> 24
#
# Candidate D: "You can make any elevator arrive instantly, but only if you are already inside it."
#   1:5 (if you are inside, it has already arrived)  2:4 (funny loop, less visual)
#   3:4 (loop structure is somewhat familiar)  4:3 (little concrete detail)  5:5  -> 21
#
# Winner: Candidate C — the only one scoring 5 on criterion 1 without quietly helping,
# and the most visual joke.
#
# Revision 1: add the unit "in Celsius" — criterion 4 (tight, specific, concrete detail).
# A bare "exact temperature" is abstract; a Celsius reading fixes the power in the world
# and makes the hero's announcement funnier to picture ("73 degrees Celsius!").

import os

ENTRY = "You can instantly know the exact temperature in Celsius of any soup you are already tasting."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
