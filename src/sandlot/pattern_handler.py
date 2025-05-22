import re
from collections.abc import Iterator

from pattern_registry import PatternRegistry


class PatternHandler:
    def __init__(self, pattern_key: str):
        self.pattern_key = pattern_key

    def findall(self, text: str, flags: int = 0) -> list[str]:
        rx = PatternRegistry.get(self.pattern_key, flags)
        return rx.findall(text)

    def search(self, text: str, flags: int = 0) -> re.Match[str] | None:
        rx = PatternRegistry.get(self.pattern_key, flags)
        return rx.search(text)

    def finditer(self, text: str, flags: int = 0) -> Iterator[re.Match[str]]:
        rx = PatternRegistry.get(self.pattern_key, flags)
        return rx.finditer(text)

    @staticmethod
    def build_pattern(keywords: Iterator[str]) -> re.Pattern:
        return "|".join(keyword for keyword in keywords)

    @property
    def pattern(self):
        return PatternRegistry.get(self.pattern_key)
