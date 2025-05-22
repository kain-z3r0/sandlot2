import re
from collections.abc import Iterator
from pathlib import Path
from typing import Protocol

from extractor import InningExtractor, PlayerExtractor, TeamExtractor
from regex_wrapper import RegexWrapper
from uid_generator import generate_uid


def _uid_replacer(match):
    return generate_uid(match.group("key"), "player")


class PlayerTransformer:
    def __init__(self, players):
        self.players_rx = RegexWrapper.build_rx(players)

    def transform(self, text: str) -> str:
        return self.players_rx.sub(_uid_replacer, text)


class TeamTransformer:
    def __init__(self):
        pass

    def transform(self):
        pass
        


def main():
    filepath = Path(__file__).resolve().parent / "simple_sample.txt"
    text = filepath.read_text()

    players = PlayerExtractor().extract(text)

    


if __name__ == "__main__":
    main()
