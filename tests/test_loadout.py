from item import Item
from loadout import Loadout

def test_loadout_contains_items():
    vandal = Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary")
    loadout = Loadout([vandal], 0.9)
    assert len(loadout.items) == 1
    assert loadout.items[0] == vandal

def test_cost():
    vandal = Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary")
    lightshields = Item("Light Shields",400,0.1,0.65,0.05,0.7,"shield")
    loadout = Loadout([vandal, lightshields], 1.0)
    assert loadout.cost() == 3300