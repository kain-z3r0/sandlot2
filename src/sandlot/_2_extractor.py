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
        self.lines_to_remove: tuple[str, ...] = ()

    def extract(self, text: str) -> tuple[str, ...]:
        self.lines_to_remove = tuple(self.line_filter_pattern.findall(text, re.MULTILINE))
        return self.lines_to_remove

    @property
    def count(self) -> int:
        return len(self.lines_to_remove)


def main():
    text = load("full_sample.txt")

    teams = TeamExtractor().extract(text)
    line_filter = LineFilter()
    lines_to_remove = line_filter.extract(text)
    


if __name__ == "__main__":
    main()
