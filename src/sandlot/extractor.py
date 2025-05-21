from regex_wrapper import RegexWrapper
from uid_generator import generate_uid  # XXX: UID generation should be moved to transformer layer

class PlayerExtractor():
    def __init__(self):
        self.players_ahead = RegexWrapper("players_ahead")
        self.players_behind = RegexWrapper("players_behind")

    def extract(self, text: str) -> set[str]:

        player_names = set(self.players_ahead.findall(text))
        player_names.update(self.players_behind.findall(text))

        return player_names


class TeamExtractor(Extractor[TeamRecord]):
    def __init__(self):
        self.inning_header_rx = RegexWrapper("inning_header")
        self.age_rx = RegexWrapper("age_bracket")
        self.teams_without_age: int = 0

    def extract(self, text: str):















































        team_lines = self.team_rx.findall(text)  # TODO: Capture entire line where team pattern match
        teams: dict[str, TeamRecord] = {}

        for line in team_lines:
            age_match = self.age_rx.search(line)
            age = age_match["age"].upper() if age_match else None
            team_name = " ".join(
                self.age_rx.pattern.sub("", line).upper().strip().split()
            )

            if team_name not in teams:
                teams[team_name] = {
                    "name": team_name,
                    "uid": generate_uid(team_name, "team"),
                    "age": age
                }
                if age is None:
                    logger.warning(f"Team '{team_name}' is missing age bracket!")
                    self.teams_without_age += 1
            elif teams[team_name]["age"] is None and age:
                teams[team_name]["age"] = age
                self.teams_without_age -= 1
                logger.info(f"Resolved age bracket for team '{team_name}': {age}")

        return {"teams": list(teams.values())}


"""
if __name__ == "__main__":
    filepath = Path(__file__).resolve().parent / "simple_example.txt"
    text = filepath.read_text()

    ext = PlayerExtractor()
    result = ext.extract(text)

    print("Extracted Player Records:\n")
    for record in result["players"]:
        print(f"Name : {record['name']}")
        print("-" * 40)

"""