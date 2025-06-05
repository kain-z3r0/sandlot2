"""
Module: extractors.py

Purpose:
    Provides lightweight, stateless extractors for pulling structured data from raw game log text.

Functions:
    - team_extractor(text): Extracts team info lines (e.g. "9U Del Boca Vista").
    - line_selector(text): Identifies lines to be removed or filtered out during preprocessing.
"""

import re

from pattern_handler import PatternHandler


def team_extractor(text: str) -> tuple[str, ...]:
    return tuple(PatternHandler("team_info").findall(text))


def line_selector(text: str) -> tuple[str, ...]:
    return tuple(PatternHandler("filter").findall(text, re.MULTILINE))


def player_extractor(text: str) -> tuple[str, ...]:
    players = set(PatternHandler("players_ahead").findall(text))
    players.update(PatternHandler("players_behind").findall(text))
    return tuple(players)


def inning_extractor(text: str) -> tuple[str, ...]:
    return tuple(PatternHandler("inning_header").findall(text))
    

from _1_loader import load

def main():
    text = load("simple_sample.txt")

    innings = inning_extractor(text)
    print(innings)


if __name__ == "__main__":
    main()
