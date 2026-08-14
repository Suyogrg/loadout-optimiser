from greedy_algorithm import GreedyAlgorithm
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

def weights():
    return {"offensive": 1.0, "defensive": 0.0, "utility": 0.0, "versatility": 0.0}

def test_greedy():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary")]
    greedy = GreedyAlgorithm()
    result = greedy.optimise(items,constraints(),weights())
    assert result.items[0].name == "A"

def test_optimise_budget():
    items = [Item("A",500,0.5,0.0,0.0,0.0,"primary"), 
             Item("B",1100,1.0,0.0,0.0,0.0,"shield")]
    greedy = GreedyAlgorithm()
    result = greedy.optimise(items,constraints(),weights())
    assert result.cost() <= 1000

def test_optimise_group():
    items = [Item("A",800,0.6,0.0,0.0,0.0,"primary"), 
             Item("B",400,0.5,0.0,0.0,0.0,"primary")]
    greedy = GreedyAlgorithm()
    result = greedy.optimise(items,constraints(),weights())
    assert len(result.items) == 1
    assert result.items[0].name == "B"

def test_empty():
    greedy = GreedyAlgorithm()
    result = greedy.optimise([],constraints(),weights())
    assert result.items == []
    assert result.cost() == 0