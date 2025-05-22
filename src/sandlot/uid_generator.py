from functools import lru_cache

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
    ordered_chars = "".join(
        char for _, char in sorted(selected_chars, key=lambda x: x[0])
    )
    return ordered_chars


def _build_team_id(name: str, id_length: int = 7) -> str:
    prefix, remaining_chars = _normalize_split_name(name)
    non_vowels, vowels = _split_chars_by_vowel_type(remaining_chars)
    chars_needed = id_length - len(prefix)
    core_name = _select_chars(non_vowels, vowels, chars_needed)
    suffix = core_name.ljust(chars_needed, "X")
    return f"TEAM_{prefix}{suffix}"


def _build_player_id(name: str, id_length: int = 7) -> str:
    normalized_name = _normalize_name(name)
    core_name = normalized_name[:id_length]
    suffix = core_name.ljust(id_length, "X")
    return f"PLAYER_{suffix}"


@lru_cache(maxsize = None)
def generate_uid(name: str, entity: str, id_length: int = 7) -> str:
    if entity == "team":
        return _build_team_id(name, id_length)
    elif entity == "player":
        return _build_player_id(name, id_length)
    else:
        raise ValueError(f"Entity type '{entity}' not supported!")
