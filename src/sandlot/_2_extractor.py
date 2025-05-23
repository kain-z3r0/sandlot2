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
    return tuple(sPatternHandler("filter").findall(text, re.MULTILINE))

