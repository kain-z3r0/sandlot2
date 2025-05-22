import re
from functools import cache


class PatternRegistry:
    # =============== Team & Inning Regex ==============================
    _INNING_HALF = r"(?:Top|Bottom)"
    _INNING_NUM = r"\d(?:st|nd|rd|th)"
    _AGE_BRACKET = r"(?P<age>\d{1,2}[Uu])\b"
    _INNING_HEADER = rf"(?P<inning>{_INNING_HALF} {_INNING_NUM}) - (?P<team_info>.+)"
    _TEAM_INFO = rf"(?:{_INNING_HALF} {_INNING_NUM} - )(?P<team_info>.+)"

    # =============== Player Regex ============================
    _VERBS_AHEAD = "|".join(
        [
            "advances",
            "caught",
            "did",
            "doubles",
            "flies",
            "gets",
            "grounds",
            "held",
            "hits",
            "homers",
            "in",
            "is",
            "lines",
            "out",
            "picked",
            "pitching",
            "pops",
            "reaches",
            "remains",
            "sacrifices",
            "scores",
            "singles",
            "steals",
            "strikes",
            "to",
            "triples",
            "walks",
        ]
    )

    _VERBS_BEHIND = "|".join(
        [
            "by catcher",
            "by pitcher",
            "by shortstop",
            "center fielder",
            "Courtesy runner",
            "first baseman",
            "for batter",
            "for pitcher",
            "in for",
            "left fielder",
            "right fielder",
            "second baseman",
            "third baseman",
            "to catcher",
            "to pitcher",
            "to shortstop",
        ]
    )

    _PLAYER_BLOCK = "|".join(
        [
            r"Unknown Player",
            r"\b[A-Z]{1,2} [A-Z][a-z]{0,15}-?[A-Za-z]{0,15}(?:\sJr)?\b",
            r"#\d{1,3}",
            r"\b[A-Z][A-Za-z]{3,10}\b",
            r"\b[A-Z][a-z]{4,10} [A-Z][a-z]{3,10}\b",
            r"\b[a-z] [a-z]\b",
        ]
    )

    _PLAYER_LOOKAHEAD = rf"(?P<name>{_PLAYER_BLOCK})(?=\s(?:{_VERBS_AHEAD}))"

    _PLAYER_LOOKBEHIND = rf"(?:{_VERBS_BEHIND}) (?P<name>{_PLAYER_BLOCK})"

    _PATTERNS: dict[str, str] = {
        "players_ahead": _PLAYER_LOOKAHEAD,
        "players_behind": _PLAYER_LOOKBEHIND,
        "inning_header": _INNING_HEADER,
        "age_bracket": _AGE_BRACKET,
        "team_info": _TEAM_INFO,
        "inning_half": _INNING_HALF,
        "inning_num": _INNING_NUM,
    }

    @classmethod
    @cache
    def get(cls, key: str, flags: int = 0) -> re.Pattern:
        return re.compile(cls._PATTERNS[key], flags)
