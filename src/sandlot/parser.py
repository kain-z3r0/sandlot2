cfrom extractor import InningExtractor, PlayerExtractor, TeamExtractor
from typing import TypedDict, NotRequired

class PlayerRecord(TypedDict):
    name: str
    uid: NotRequired[str | None]

class TeamRecord(TypedDict):
    name: str
    uid: NotRequired[str | None]
    age: str


class PlayerParser:

    def parse(self, data: set[str]) -> dict[str, PlayerRecord]:
        return {player: {"name": player} for player in data}


class TeamParser:

    def parse(self, data: set[str]) -> dict[str, TeamRecord]:
        return {
            team: {
                "name": team,
                "age": 
            }
        }




from pathlib import Path
def main():
    filepath = Path(__file__).resolve().parent / "simple_sample.txt"
    text = filepath.read_text()

    players_raw = PlayerExtractor().extract(text)
    print(players_raw)

    players = PlayerParser().parse(players_raw)
    print(players)


if __name__ == "__main__":
    main()