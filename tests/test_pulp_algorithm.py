from item import Item
from pulp_algorithm import PulpAlgorithm

def test_optimise_budget():
    items = [Item("A",100,0.5,0.0,0.0,0.0,"primary"), 
             Item("B",200,1.0,0.0,0.0,0.0,"primary")]
    weights = {"offensive": 1.0, "defensive": 0.0, "utility": 0.0, "versatility": 0.0}
    constraints = {
        "budget": 100,
        "primary": 1,
        "secondary": 0,
        "shield": 0,
        "ability1": 0,
        "ability2": 0,
        "ability3": 0
    }
    optimiser = PulpAlgorithm()
    loadout = optimiser.optimise(items, constraints, weights)
    assert loadout.cost() <= 100
    assert loadout.items[0].name == "A"

def test_optimise_primary():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), 
             Item("B",400,1.0,0.0,0.0,0.0,"primary")]
    weights = {"offensive": 1.0, "defensive": 0.0, "utility": 0.0, "versatility": 0.0}
    constraints = {
        "budget": 1000,
        "primary": 1,
        "secondary": 0,
        "shield": 0,
        "ability1": 0,
        "ability2": 0,
        "ability3": 0
    }
    optimiser = PulpAlgorithm()
    loadout = optimiser.optimise(items, constraints, weights)
    assert len(loadout.items) == 1
    assert loadout.items[0].name == "B"

def test_optimise_ability():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), 
             Item("B",400,1.0,0.0,0.0,0.0,"ability1","2","Jett"),
             Item("B",400,1.0,0.0,0.0,0.0,"ability1","2","Jett"),
             Item("B",400,1.0,0.0,0.0,0.0,"ability1","2","Jett")]
    weights = {"offensive": 1.0, "defensive": 0.0, "utility": 0.0, "versatility": 0.0}
    constraints = {
        "budget": 1000,
        "primary": 0,
        "secondary": 0,
        "shield": 0,
        "ability1": 2,
        "ability2": 0,
        "ability3": 0
    }
    optimiser = PulpAlgorithm()
    loadout = optimiser.optimise(items, constraints, weights)
    assert len(loadout.items) == 2
    assert loadout.cost() == 800
    assert loadout.items[0].name == "B"