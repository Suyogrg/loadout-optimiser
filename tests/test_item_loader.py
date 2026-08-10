from item_loader import load_items, get_items

def test_load_items():
    items = load_items()
    assert isinstance(items, list)
    assert len(items) > 0

def test_get_items_agent():
    items = [
        {"name": "Vandal", "cost": 2900, "offensive": 0.9, "defensive": 0.25, "utility": 0.2, "versatility": 0.95, "group": "primary"},
        {"name": "Cloudburst", "cost": 200, "offensive": 0.2, "defensive": 0.75, "utility": 0.7, "versatility": 0.65, "group": "ability1", "slots": 2, "agent": "Jett"},
        {"name": "Shrouded Step", "cost": 100, "offensive": 0.2, "defensive": 0.6, "utility": 0.45, "versatility": 0.65, "group": "ability1", "slots": 2, "agent": "Omen"}
    ]
    result = get_items(items, 3000, "Jett")

    assert len(result) == 2
    assert result[0]["name"] == "Vandal"
    assert result[1]["name"] == "Cloudburst"

def test_get_items_credit():
    items = [
        {"name": "Vandal", "cost": 2900, "offensive": 0.9, "defensive": 0.25, "utility": 0.2, "versatility": 0.95, "group": "primary"},
        {"name": "Outlaw", "cost": 2400, "offensive": 0.85, "defensive": 0.2, "utility": 0.45, "versatility": 0.2, "group": "primary"},
        {"name": "Bandit", "cost": 600, "offensive": 0.5, "defensive": 0.05, "utility": 0.05, "versatility": 0.5, "group": "secondary"},
    ]
    result = get_items(items, 2500, "Jett")

    assert len(result) == 2
    assert result[0]["name"] == "Outlaw"
    assert result[1]["name"] == "Bandit"