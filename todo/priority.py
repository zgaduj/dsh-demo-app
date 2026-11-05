"""Priority filtering for a tiny to-do list."""

LEVELS = {"low": 1, "normal": 2, "high": 3}


def parse_level(name: str) -> int:
    """Return the numeric weight of a priority level name."""
    return LEVELS[name]


def higher_than(items: list[dict], level: str) -> list[dict]:
    """Return items whose priority is strictly higher than `level`."""
    weight = parse_level(level)
    return [item for item in items if parse_level(item["priority"]) > weight]


def label(item: dict) -> str:
    """Human-readable one-line label."""
    return f"[{item['priority']}] {item['title']}"
