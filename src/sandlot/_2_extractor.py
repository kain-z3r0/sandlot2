import re

from _1_loader import load
from pattern_handler import PatternHandler


class TeamExtractor:
    def __init__(self):
        self.team_info_pattern = PatternHandler("team_info")

    def extract(self, text: str) -> tuple[str, ...]:
        return tuple(self.team_info_pattern.findall(text))


class LineFilter:
    def __init__(self):
        self.line_filter_pattern = PatternHandler("filter")
        self._lines_to_remove: tuple[str, ...] = ()

    def extract(self, text: str) -> tuple[str, ...]:
        self._lines_to_remove = tuple(self.line_filter_pattern.findall(text, re.MULTILINE))
        return self._lines_to_remove

    @property
    def count(self) -> int:
        return len(self._lines_to_remove)


def main():
    text = load("full_sample.txt")

    teams = TeamExtractor().extract(text)
    line_filter = LineFilter()
    lines_to_remove = line_filter.extract(text)
    for line in lines_to_remove:
        print(line)

    print(line_filter.count)


if __name__ == "__main__":
    main()
