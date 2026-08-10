from item import Item
from value import calculate

def test_calculate_utility():
    item = Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary")
    weights = {"offensive": 0.5, "defensive": 0.2, "utility": 0.15, "versatility": 0.15}
    result = calculate(item, weights)
    assert result == 0.6725