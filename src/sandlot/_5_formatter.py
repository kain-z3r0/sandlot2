def formatter(entity: dict[str, dict[str, str]], attr) -> list[dict[str, str]]:
    for k, v in entity.items():
        {v[attr]: d}


d = {
    "ABC 10u": {"name": "ABC 10u", "age": "10U", "uid": "TEAM_ABCXX"},
    "Golds 9U": {"name": "Golds 9U", "age": "9U", "uid": "TEAM_GOLDS"},
}


formatter(d)
