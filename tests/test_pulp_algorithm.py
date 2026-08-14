from item import Item
from pulp_algorithm import PulpAlgorithm

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

def weights():
    return {"offensive": 1.0, "defensive": 0.0, "utility": 0.0, "versatility": 0.0}

def test_optimise():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary")]
    optimiser = PulpAlgorithm()
    loadout = optimiser.optimise(items, constraints(), weights())
    assert loadout.items[0].name == "A"

def test_optimise_budget():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), 
             Item("B",1100,1.0,0.0,0.0,0.0,"shield")]
    optimiser = PulpAlgorithm()
    loadout = optimiser.optimise(items, constraints(), weights())
    assert loadout.cost() <= 1000

def test_optimise_primary():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), 
             Item("B",400,1.0,0.0,0.0,0.0,"primary")]
    optimiser = PulpAlgorithm()
    loadout = optimiser.optimise(items, constraints(), weights())
    assert len(loadout.items) == 1
    assert loadout.items[0].name == "B"

def test_optimise_ability():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), 
             Item("B",400,1.0,0.0,0.0,0.0,"ability1","2","Jett"),
             Item("B",400,1.0,0.0,0.0,0.0,"ability1","2","Jett"),
             Item("B",400,1.0,0.0,0.0,0.0,"ability1","2","Jett")]
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
    loadout = optimiser.optimise(items, constraints, weights())
    assert len(loadout.items) == 2
    assert loadout.cost() == 800
    assert loadout.items[0].name == "B"

def test_empty():
    optimiser = PulpAlgorithm()
    result = optimiser.optimise([],constraints(),weights())
    assert result.items == []
    assert result.cost() == 0