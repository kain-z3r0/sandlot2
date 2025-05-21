from extractor import PlayerExtractor, TeamExtractor, PlayerRecord
from pathlib import Path
from typing import Protocol


class PlayerTransformer:

    def __init__(self):
        pass


    def transform(self):

        






def main():
    filepath = Path(__file__).resolve().parent / "game_sample.txt"
    text = filepath.read_text()

    players = PlayerExtractor().extract(text)
    teams = TeamExtractor().extract(text)

    print(teams)
    print(players)
if __name__ == "__main__":
    main()