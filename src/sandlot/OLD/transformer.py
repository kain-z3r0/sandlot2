import re
from collections.abc import Callable, Iterator
from parser import PlayerParser, TeamParser
from pathlib import Path
from typing import Protocol

from extractor import InningExtractor, PlayerExtractor, TeamExtractor
from regex_wrapper import RegexWrapper
from uid_generator import generate_uid


class PlayerTransformer:
    def transform(self, players: set[str], text: str) -> str:
        self.players_rx = RegexWrapper.build_rx(players)
        replacer = _uid_replacer("player")
        return self.players_rx.sub(replacer, text)


class TeamTransformer:
    def transform(self, teams: set[str], text: str) -> str:
        self.team_rx = RegexWrapper.build_rx(teams)
        replacer = _uid_replacer("team")
        return self.team_rx.sub(replacer, text)

class InningTransformer:
    def transform(self, inning_headers: set[str], text: str) -> str:
        self.inning_rx = RegexWrapper.build_rx(inning_headers)
        return self.inning_rx.sub(self.normalize_inning, text)

    def normalize_inning(self, match):
        tag = "INNING_HALF_"
        inning = match.group("key")
        return f"{tag}{"".join(inning.upper().split())}"





def main():
    filepath = Path(__file__).resolve().parent / "simple_sample.txt"
    text = filepath.read_text()

    players = PlayerExtractor().extract(text)
    updated_text = PlayerTransformer().transform(players, text)

    teams = TeamExtractor().extract(text)
    updated_text = TeamTransformer().transform(teams, updated_text)
    

    innings_raw = InningExtractor().extract(updated_text)
    updated_text = InningTransformer().transform(innings_raw, updated_text)
    print(updated_text)


if __name__ == "__main__":
    main()
