from typing import TypedDict

from loguru import logger

from _1_loader import load
from _2_extractor import TeamExtractor
from pattern_handler import PatternHandler
from uid_generator import generate_uid


class TeamRecord(TypedDict):
    name: str
    uid: str
    age: str | None


class TeamTransformer:
    def __init__(self):
        self.age_pattern = PatternHandler("age_bracket")

    def transform(self, teams: tuple[str, ...]) -> list[dict[str, TeamRecord]]:
        teams_db = {}
        for team_info in teams:
            age_match = self.age_pattern.search(team_info)
            age = age_match.group("age").upper() if age_match else None
            team_name = " ".join(self.age_pattern.pattern.sub("", team_info).upper().split())

            if team_name not in teams_db:
                teams_db[team_name] = {
                    "name": team_name,
                    "uid": generate_uid(team_name, "team"),
                    "age": age,
                }
                if age is None:
                    logger.warning(f"Age missing for: {team_name}")
            elif teams_db[team_name]["age"] is None and age is not None:
                teams_db[team_name]["age"] = age
                logger.info(f"Found and updated age for team: {team_name}")

        return list(teams_db.values())


def main():
    text = load("simple_sample.txt")

    teams = TeamExtractor().extract(text)
    transformed_teams = TeamTransformer().transform(teams)

    print(transformed_teams)

if __name__ == "__main__":
    main()
