from functools import cache
from pattern_handler import PatternHandler
from collections.abc import Callable

__all__ = ["generate_id"]

VOWELS = frozenset("AEIOUY")


def _normalize_name(name: str) -> str:
    return "".join(char.upper() for char in name if char.isalnum())


def _normalize_split_name(name: str) -> tuple[str, str]:
    prefix_len = 2
    normalized_name = _normalize_name(name)
    prefix = normalized_name[:prefix_len]
    core_name = normalized_name[prefix_len:]
    return prefix, core_name


def _split_chars_by_vowel_type(core_name: str):
    non_vowels = []
    vowels = []
    for idx, char in enumerate(core_name):
        (vowels if char in VOWELS else non_vowels).append((idx, char))
    return non_vowels, vowels


def _select_chars(non_vowels, vowels, chars_needed: int) -> str:
    selected_chars = non_vowels[:chars_needed]
    vowel_count = max(0, chars_needed - len(selected_chars))
    selected_chars += vowels[:vowel_count]
    ordered_chars = "".join(char for _, char in sorted(selected_chars, key=lambda x: x[0]))
    return ordered_chars


def _build_team_id(name: str) -> str:
    id_length: int = 7
    prefix, remaining_chars = _normalize_split_name(name)
    non_vowels, vowels = _split_chars_by_vowel_type(remaining_chars)
    chars_needed = id_length - len(prefix)
    core_name = _select_chars(non_vowels, vowels, chars_needed)
    suffix = core_name.ljust(chars_needed, "X")
    return f"TEAM_{prefix}{suffix}"


def _build_player_id(name: str) -> str:
    id_length: int = 7
    normalized_name = _normalize_name(name)
    core_name = normalized_name[:id_length]
    suffix = core_name.ljust(id_length, "X")
    return f"PLAYER_{suffix}"

def _build_inning_id(inning: str) -> str:
    half = PatternHandler("inning_half").search(inning)
    num = PatternHandler("inning_num").search(inning)
    return f"INNHALF_{half} INNNUM_{num}"

# Dispatch map
_uid_builders: dict[str, Callable[..., str]] = {
    "team": _build_team_id,
    "player": _build_player_id,
    "inning": _build_inning_id
}

@cache
def generate_uid(value: str, entity: str, id_length: int = 7) -> str:
    if entity == "team":
        return _build_team_id(value, id_length)
    elif entity == "player":
        return _build_player_id(value, id_length)
    elif entity == "inning":
        return _build_inning_id(value)
    else:
        raise ValueError(f"Entity type '{entity}' not supported!")
