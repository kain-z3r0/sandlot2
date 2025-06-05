"""
Module: transformers.py

Purpose:
    Transforms extracted raw team lines into structured team records with generated UIDs.
    This module preserves the original raw text lines as dictionary keys to enable exact
    lookup and replacement in later rewriting stages of the pipeline.

Key Responsibilities:
    - Parse team lines to extract team name and optional age bracket.
    - Generate a unique ID (UID) for each team.
    - Build a mapping from raw line → structured TeamRecord (name, uid, age).
    - Handle missing age info and update entries if better age data is found.

Note:
    This transformer is designed to support exact text replacement by keeping the original
    raw lines as keys in the returned dictionary. This ensures safe and accurate rewriting
    of the game logs downstream.
"""

# TODO: Create a transformer for player lines
#   - Extract player names using player regex patterns
#   - Normalize names
#   - Generate player UIDs
#   - Store mapping from raw line → structured PlayerRecord

# TODO: Create a transformer for inning metadata
#   - Extract inning number and half
#   - Normalize as tags or structured fields
#   - Generate UID or tag label
#   - Store mapping from raw inning line → structured InningRecord

# TODO: Create a transformer for events


# XXX: Ensure each transformer keeps raw lines as keys
#    - This enables safe lookup during text rewriting
#    - Raw line → UID mapping must be exact to avoid incorrect replacements

from typing import TypedDict

from pattern_handler import PatternHandler
from uid_generator import generate_uid


class TeamRecord(TypedDict):
    name: str
    uid: str
    age: str | None

class PlayerRecord(TypedDict):
    name: str
    uid: str

class InningRecord(TypedDict):
    tag: str

def team_transformer(raw_team_lines: tuple[str, ...]) -> dict[str, TeamRecord]:
    team_records: dict[str, TeamRecord] = {}
    age_pattern = PatternHandler("age_bracket")

    for raw_line in raw_team_lines:
        team_name, age = _split_team_name_age(raw_line, age_pattern)
        record = team_records.setdefault(
            raw_line, {"name": team_name, "uid": generate_uid(team_name, "team"), "age": age}
        )
        if record["age"] is None and age is not None:
            record["age"] = age
    return team_records


def _split_team_name_age(line: str, age_pattern: PatternHandler) -> tuple[str, str | None]:
    age_match = age_pattern.search(line)
    age = age_match.group("age").upper() if age_match else None
    team_name = " ".join(age_pattern.sub("", line).upper().split())
    return team_name, age

def player_transformer(players: tuple[str, ...]) -> dict[str, PlayerRecord]:
    player_records: dict[str, PlayerRecord] = {}

    for player in players:
        record = player_records.setdefault(
            player, {"name": player, "uid": generate_uid(player, "player")}
        )

    return player_records

def inning_transformer(innings: tuple[str, ...]) -> dict[str, InningRecord]:
    inn_half = PatternHandler("inning_half").search(innings)
    inn_num = PatternHandler("inning_num").search(innings)

    inn_records: dict[str, InningRecord] = {}

    for inning in innings:
        half = 
        record = inn_records.setdefault(
            inning, {"half": }
        )



from _1_loader import load
from _2_extractor import team_extractor, line_selector, player_extractor, inning_extractor


def main():
    text = load("simple_sample.txt")
    teams = team_extractor(text)
    lines = line_selector(text)
    trans = team_transformer(teams)
    players = player_extractor(text)
    pt = player_transformer(players)
    inns = inning_extractor(text)
    print(inns)



if __name__ == "__main__":
    main()
