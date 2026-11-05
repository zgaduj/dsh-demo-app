from todo import priority

ITEMS = [
    {"title": "write docs", "priority": "low"},
    {"title": "fix bug", "priority": "high"},
    {"title": "review PR", "priority": "normal"},
]


def test_levels_ordered():
    assert priority.parse_level("low") < priority.parse_level("high")


def test_higher_than_high_is_empty():
    assert priority.higher_than(ITEMS, "high") == []


def test_higher_than_normal():
    assert [i["title"] for i in priority.higher_than(ITEMS, "normal")] == ["fix bug"]
