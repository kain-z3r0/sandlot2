from typing import Protocol, TypedDict, TypeVar, Generic
from pathlib import Path
from regex_wrapper import RegexWrapper
from loguru import logger
from uid_generator import generate_uid

def _normalize_name(name: str) -> str:
    pass
    # alnum_chars = "".join(char for char in name if char.isalnum() or char in (" ", "-"))
    # return " ".join(alnum_chars.title().strip().split())


class PlayerRecord(TypedDict):
    name: str
    uid: str | None


class TeamRecord(TypedDict):
    name: str
    uid: str | None
    age: str | None


T = TypeVar("T", bound=dict)


class Extractor(Protocol, Generic[T]):
    def extract(self, text: str) -> dict[str, list[T]]: ...


class PlayerExtractor(Extractor[PlayerRecord]):
    def __init__(self):
        self.players_ahead = RegexWrapper("players_ahead")
        self.players_behind = RegexWrapper("players_behind")

    def extract(self, text: str) -> dict[str, list[PlayerRecord]]:
        players_raw = set(self.players_ahead.findall(text))
        players_raw.update(self.players_behind.findall(text))

        players: dict[str, PlayerRecord] = {}
        for player in players_raw:
            player_name = _normalize_name(player)
            players[player_name] = {"name": player_name, "uid": generate_uid(player_name, "player")}

        return {"players": list(players.values())}


class TeamExtractor(Extractor[TeamRecord]):
    def __init__(self):
        self.team_rx = RegexWrapper("team_info")
        self.age_rx = RegexWrapper("age_bracket")
        self.teams_missing_age_cnt: int = 0

    def extract(self, text: str) -> dict[str, list[TeamRecord]]:
        team_lines = self.team_rx.findall(text)
        teams: dict[str, TeamRecord] = {}

        for line in team_lines:
            age_match = self.age_rx.search(line)
            age = age_match["age"].upper() if age_match else None
            team_name = " ".join(
                self.age_rx.pattern.sub("", line).upper().strip().split()
            )

            if team_name not in teams:
                teams[team_name] = {"name": team_name, "uid": generate_uid(team_name, "team"), "age": age}
                if age is None:
                    logger.warning(f"Team '{team_name}' is missing age bracket!")
                    self.teams_missing_age_cnt += 1
            elif teams[team_name]["age"] is None and age:
                teams[team_name]["age"] = age
                self.teams_missing_age_cnt -= 1
                logger.info(f"Resolved age bracket for team '{team_name}': {age}")

        return {"teams": list(teams.values())}


"""
if __name__ == "__main__":
    filepath = Path(__file__).resolve().parent / "game_sample.txt"
    text = filepath.read_text()

    ext = TeamExtractor()
    teams = ext.extract(text)
    print(f"Teams missing age: {ext.teams_missing_age_cnt}")
"""