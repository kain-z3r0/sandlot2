from extractor import InningExtractor, PlayerExtractor, TeamExtractor
from typing import TypedDict, NotRequired
from regex_wrapper import RegexWrapper
from loguru import logger

def get_age(data):
    age_match = RegexWrapper("age_bracket").search(data)
    if not age_match:
        return None
    return age_match.group("age")

def get_team_name(data):
    age_rx = RegexWrapper("age_bracket")
    return " ".join(age_rx.pattern.sub("", data).split())


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
        team_data = {}
        for team in data:
            age = get_age(team)
            name = get_team_name(team)
            
            if name not in team_data:
                team_data[name] = {"name": name, "age": age}
                logger.info(f"Found team: {name}")
                if age is None:
                    logger.warning(f"Team {name} is missing age bracket!")
            elif age is not None and team_data[name]["age"] is None:
                logger.info(f"Age updated for team '{name}'")
                team_data[name]["age"] = age    
        return team_data






from pathlib import Path
def main():
    filepath = Path(__file__).resolve().parent / "simple_sample.txt"
    text = filepath.read_text()

    players_raw = PlayerExtractor().extract(text)
    players = PlayerParser().parse(players_raw)

    teams_raw = TeamExtractor().extract(text)
    teams = TeamParser().parse(teams_raw)
    print(teams)



if __name__ == "__main__":
    main()