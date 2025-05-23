import re

from _1_loader import load
from pattern_handler import PatternHandler


class TeamExtractor:
    def __init__(self):
        self.team_info_pattern = PatternHandler("team_info")

    def extract(self, text: str) -> tuple[str, ...]:
        return tuple(self.team_info_pattern.findall(text))
    

class LineSelector:
    def __init__(self):
        self.line_filter_pattern = PatternHandler("filter")

    def extract(self, text: str) -> tuple[str, ...]:
        return tuple(self.line_filter_pattern.findall(text, re.MULTILINE))
    

def main():
    text = load("full_sample.txt")

    
    

if __name__ == "__main__":
    main()
