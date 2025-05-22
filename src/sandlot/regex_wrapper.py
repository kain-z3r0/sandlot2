import re
from collections.abc import Iterator

from regex_registry import RegexRegistry


class RegexWrapper:
    def __init__(self, pattern_key: str):
        self.pattern_key = pattern_key

    def findall(self, text: str, flags: int = 0) -> list[str]:
        rx = RegexRegistry.get(self.pattern_key, flags)
        return rx.findall(text)

    def search(self, text: str, flags: int = 0) -> re.Match[str] | None:
        rx = RegexRegistry.get(self.pattern_key, flags)
        return rx.search(text)

    def finditer(self, text: str, flags: int = 0) -> Iterator[re.Match[str]]:
        rx = RegexRegistry.get(self.pattern_key, flags)
        return rx.finditer(text)

    @staticmethod
    def build_rx(keywords: Iterator[str]) -> re.Pattern:
        return RegexRegistry.build_pattern(keywords)

    @property
    def pattern(self):
        return RegexRegistry.get(self.pattern_key)
