from _1_loader import load
from _2_extractor import team_extractor
from _3_transformer import team_transformer
from _4_text_rewriter import replacer





class GameParser:

    def __init__(self):
        self.gamelog = None


    def run(self, text: str) -> None:
        teams_raw = team_extractor(text)
        teams_trans = team_transformer(teams_raw)
        self.gamelog = replacer(text, teams_trans, "uid")







text = load("simple_sample.txt")

parser = GameParser()
parser.run(text)


print(parser.gamelog)