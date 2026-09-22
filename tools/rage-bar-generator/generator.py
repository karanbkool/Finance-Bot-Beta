#!/usr/bin/env python3
"""Random rage/trap bar generator.

Assembles original bars from line templates and word banks (Mad-Libs
style). Nothing here is copied or derived from any specific artist's
lyrics -- it's all original vocabulary and templates meant to riff on
the rage/trap aesthetic (ad-libs, flex lines, dark imagery, slang).
"""

import argparse
import random

AD_LIBS = [
    "yeah", "huh", "ayy", "let's go", "on god", "straight up",
    "no cap", "skrrt", "woo", "uh-huh", "for real", "go crazy",
]

SUBJECTS = [
    "I", "we", "my whole team", "my squad", "the opps", "these n****",
    "my ex", "the label", "my shooters", "the industry",
]

FLEX_VERBS = [
    "pull up in", "stack", "flip", "count", "push", "drip in",
    "touch down with", "cop", "flood the closet with", "stunt on 'em with",
]

FLEX_NOUNS = [
    "a brand new foreign", "six figures", "a fresh check", "ice on ice",
    "a whole new fit", "designer from head to toe", "a rented Rolls",
    "a stack of bands", "custom diamonds", "a closet full of heat",
]

DARK_IMAGERY = [
    "shadows on the wall", "static in my head", "smoke behind the glass",
    "ghosts in the studio", "sirens in the distance", "static on the beat",
    "a storm behind my eyes", "chrome under the seat", "voices in the mix",
    "a fire in my chest",
]

ATTITUDE = [
    "and I don't feel a thing", "but I keep it moving",
    "and nobody can stop it", "so I never look back",
    "and that's just how it is", "but I stay in my zone",
    "and the world keeps spinning", "so I turn it up louder",
    "and I ride it out alone", "but I never flinch",
]

BRAGS = [
    "outworked everybody in the room",
    "turned the pain into a hit record",
    "built this whole thing from nothing",
    "never needed nobody's co-sign",
    "made it out and never looked back",
    "wrote my way out the dark",
    "stayed up till the sun came through the blinds",
    "turned static into a symphony",
]

TEMPLATES = [
    "{adlib}, {subject} {verb} {noun}",
    "{subject} got {imagery}, {attitude}",
    "{subject} {brag}",
    "{adlib} -- {subject} {verb} {noun}, {attitude}",
    "{imagery} in the rearview, {subject} {brag}",
    "{subject} {verb} {noun} {attitude}",
]


def make_line():
    return TEMPLATES[random.randrange(len(TEMPLATES))].format(
        adlib=random.choice(AD_LIBS).capitalize(),
        subject=random.choice(SUBJECTS),
        verb=random.choice(FLEX_VERBS),
        noun=random.choice(FLEX_NOUNS),
        imagery=random.choice(DARK_IMAGERY).capitalize(),
        attitude=random.choice(ATTITUDE),
        brag=random.choice(BRAGS),
    )


def make_verse(lines=8):
    return [make_line() for _ in range(lines)]


def main():
    parser = argparse.ArgumentParser(description="Random rage/trap bar generator")
    parser.add_argument("-n", "--lines", type=int, default=8, help="number of lines to generate")
    parser.add_argument("-s", "--seed", type=int, default=None, help="random seed for reproducible output")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    for line in make_verse(args.lines):
        print(line)


if __name__ == "__main__":
    main()
