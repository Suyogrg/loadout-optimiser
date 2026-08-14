from loadout_service import get_agents, generate
from item import Item

def test_get_agents():
    items = [Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary"),
             Item("Cloudburst",200,0.2,0.75,0.7,0.65,"ability1",2,"Jett"),
             Item("Updraft",150,0.2,0.45,0.4,0.35,"ability2",1,"Jett"),
             Item("Paraonia",250,0.7,0.7,0.85,0.7,"ability2",1,"Omen")]
    result = get_agents(items)
    assert result == ["Jett", "Omen"]

def test_generate_abilities():
    items = [Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary"),
             Item("Cloudburst",200,0.2,0.75,0.7,0.65,"ability1",2,"Jett"),
             Item("Updraft",150,0.2,0.45,0.4,0.35,"ability2",1,"Jett"),
             Item("Paraonia",250,0.7,0.7,0.85,0.7,"ability2",1,"Omen")]
    weights = {"offensive": 0.25, "defensive": 0.25, "utility": 0.25, "versatility": 0.25}
    result = generate(items,"Jett",5000,weights)
    assert all(item.agent == "Jett" or item.agent is None for item in result.items)

def test_generate_budget():
    items = [Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary"),
             Item("Cloudburst",200,0.2,0.75,0.7,0.65,"ability1",2,"Jett"),
             Item("Updraft",150,0.2,0.45,0.4,0.35,"ability2",1,"Jett"),
             Item("Paraonia",250,0.7,0.7,0.85,0.7,"ability2",1,"Omen")]
    weights = {"offensive": 0.25, "defensive": 0.25, "utility": 0.25, "versatility": 0.25}
    result = generate(items,"Jett",3100,weights)
    assert result.cost() <= 3100