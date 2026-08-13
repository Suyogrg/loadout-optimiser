from validation import is_valid
from item import Item

def constraints():
    return {
        "budget": 1000,
        "primary": 1,
        "secondary": 1,
        "shield": 1,
        "ability1": 1,
        "ability2": 1,
        "ability3": 1
        }

def test_is_valid():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), Item("B",400,0.4,0.0,0.0,0.0,"shield")]
    assert is_valid(items, constraints())

def test_over_budget():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), Item("B",400,0.4,0.0,0.0,0.0,"primary")]
    assert not is_valid(items, constraints())

def test_over_group():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), Item("B",400,0.4,0.0,0.0,0.0,"primary")]
    assert not is_valid(items, constraints())

def test_empty_loadout_is_valid():
    assert is_valid([], constraints())

