from todo import priority

ITEMS = [
    {"title": "write docs", "priority": "low"},
    {"title": "fix bug", "priority": "high"},
    {"title": "review PR", "priority": "normal"},
]


def test_sorted_high_first():
    titles = [i["title"] for i in priority.sort_by_priority(ITEMS)]
    assert titles == ["fix bug", "review PR", "write docs"]


def test_sort_does_not_mutate_input():
    before = list(ITEMS)
    priority.sort_by_priority(ITEMS)
    assert ITEMS == before
