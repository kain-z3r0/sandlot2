from _1_loader import load
from _2_extractor import team_extractor, player_extractor
from _3_transformer import team_transformer, line_selector, player_transformer
from _4_text_rewriter import replacer, skip_line


class GameParser:
    def __init__(self):
        self.gamelog = None

    def run(self, text: str) -> None:
        teams_raw = team_extractor(text)
        teams_trans = team_transformer(teams_raw)
        self.gamelog = replacer(text, teams_trans, "uid")
        lines = line_selector(text)
        self.gamelog = skip_line(self.gamelog, lines)
        players_raw = player_extractor(text)
        players_trans = player_transformer(players_raw)
        self.gamelog = replacer(self.gamelog, players_trans, "uid")




text = load("simple_sample.txt")

parser = GameParser()
parser.run(text)


print(parser.gamelog)
