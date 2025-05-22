from regex_wrapper import RegexWrapper


class PlayerExtractor:
    def __init__(self):
        self.players_ahead = RegexWrapper("players_ahead")
        self.players_behind = RegexWrapper("players_behind")

    def extract(self, text: str) -> set[str]:
        player_names = set(self.players_ahead.findall(text))
        player_names.update(self.players_behind.findall(text))

        return player_names


class TeamExtractor:
    def __init__(self):
        self.inning_header_rx = RegexWrapper("inning_header")

    def extract(self, text: str) -> set[str]:
        team_data = set()
        for match in self.inning_header_rx.finditer(text):
            team_data.add(match.group("team_info"))

        return team_data


class InningExtractor:
    def __init__(self):
        self.inning_header_rx = RegexWrapper("inning_header")

    def extract(self, text: str) -> set[str]:
        inning_info = set()

        for match in self.inning_header_rx.finditer(text):
            inning_info.add(match.group("inning"))

        return inning_info



# from pathlib import Path
# from regex_registry import RegexRegistry
# if __name__ == "__main__":
#     filepath = Path(__file__).resolve().parent / "simple_sample.txt"
#     text = filepath.read_text()
#     ext = PlayerExtractor()
#     players = ext.extract(text)
#     print(players)

#     ext = TeamExtractor()
#     teams = ext.extract(text)

#     ext = InningExtractor()
#     innings = ext.extract(text)
#     print(innings)
#     print(teams)
#     print(f"Regex cache usage: {RegexRegistry.get.cache_info()}")
