from item_loader import load_items, get_items
from item import Item

def test_load_items():
    items = load_items()
    assert len(items) > 0
    for item in items:
        assert isinstance(item, Item)

def test_load_items_contains_vandal():
    items = load_items()
    vandal = next(item for item in items if item.name == "Vandal")
    assert vandal.cost == 2900
    assert vandal.offensive == 0.9
    assert vandal.group == "primary"

def test_get_items_by_agent():
    vandal = Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary")
    cloudburst = Item("Cloudburst",200,0.2,0.75,0.7,0.65,"ability1",2,"Jett")
    shroudedstep = Item("Shrouded Step",100,0.2,0.6,0.45,0.65,"ability1",2,"Omen")
    items = [vandal,cloudburst,shroudedstep]
    result = get_items(items, 5000, "Jett")
    assert len(result) == 2
    assert result[0].name == "Vandal"
    assert result[1].name == "Cloudburst"

def test_get_items_by_credit():
    vandal = Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary")
    outlaw = Item("Outlaw",2400,0.85,0.2,0.45,0.2,"primary")
    bandit = Item("Bandit",600,0.5,0.05,0.05,0.5,"secondary")
    items = [vandal,outlaw,bandit]
    result = get_items(items, 2500, "Jett")
    assert len(result) == 2
    assert result[0].name == "Outlaw"
    assert result[1].name == "Bandit"