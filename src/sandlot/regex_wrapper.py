from regex_registry import RegexRegistry
from re import Match


class RegexWrapper:
    def __init__(self, pattern_key: str):
        self.pattern_key = pattern_key

    def findall(self, text: str, flags: int = 0) -> list[str]:
        rx = RegexRegistry.get(self.pattern_key, flags)
        return rx.findall(text)

    def search(self, text: str, flags: int = 0) -> Match[str] | None:
        rx = RegexRegistry.get(self.pattern_key, flags)
        return rx.search(text)

    @property
    def pattern(self):
        return RegexRegistry.get(self.pattern_key)
