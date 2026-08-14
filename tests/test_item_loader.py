from item_loader import load_items
from item import Item

def test_load_items():
    items = load_items()
    assert len(items) > 0
    for item in items:
        assert isinstance(item, Item)

def test_load_items_vandal():
    items = load_items()
    vandal = next(item for item in items if item.name == "Vandal")
    assert vandal.name == "Vandal"

def test_load_items_multiple_abilites():
    items = load_items()
    count = []
    for item in items:
        if item.name == "Shrouded Step":
            count.append(item)
    assert len(count) == 2
