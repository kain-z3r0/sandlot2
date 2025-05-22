import re
from collections.abc import Iterable
from functools import cache, cached_property

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

    def finditer(self, text: str, flags: int = 0) -> Iterable[re.Match[str]]:
        rx = PatternRegistry.get(self.pattern_key, flags)
        return rx.finditer(text)

    @cached_property
    def pattern(self):
        return PatternRegistry.get(self.pattern_key)


@cache
def compile_entity_pattern(entities: Iterable[str]) -> re.Pattern:
    joined = "|".join(tuple(entities))
    return re.compile(rf"(?P<entity>{joined})")
