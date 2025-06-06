from _1_loader import load
from _2_extractor import team_extractor, player_extractor, inning_extractor
from _3_transformer import team_transformer, line_selector, player_transformer, inning_transformer
from _4_text_rewriter import replacer, skip_line


class TextNormalizer:
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
        inns_raw = inning_extractor(text)
        inns_trans = inning_transformer(inns_raw)
        self.gamelog = replacer(self.gamelog, inns_trans, "uid", False)


    @property
    def text(self):
        return self.gamelog



text = load("simple_sample.txt")

parser = TextNormalizer()
parser.run(text)


normalized_text = parser.text

print(parser.gamelog)





