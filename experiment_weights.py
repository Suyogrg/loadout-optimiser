import pandas as pd
from pulp_algorithm import PulpAlgorithm
from item_loader import load_items

def main():
    items = load_items()
    filtered = [item for item in items if item.agent == "Omen" or item.agent == None]
    constraints = {
        "budget": 5000,
        "primary": 1,
        "secondary": 1,
        "shield": 1,
        "ability1": 2,
        "ability2": 1,
        "ability3": 1
    }
    weights = {
        "balanced": {"offensive": 0.25, "defensive": 0.25,"utility": 0.25, "versatility": 0.25},
        "offensive": {"offensive": 0.70, "defensive": 0.10, "utility": 0.10, "versatility": 0.10},
        "defensive": {"offensive": 0.10, "defensive": 0.70, "utility": 0.10, "versatility": 0.10},
        "utility": {"offensive": 0.10, "defensive": 0.10, "utility": 0.70, "versatility": 0.10},
        "versatility": {"offensive": 0.10, "defensive": 0.10, "utility": 0.10, "versatility": 0.70}
    }
    results = []
    algorithm = PulpAlgorithm()
    for model_name, weight in weights.items():
        loadout = algorithm.optimise(filtered, constraints, weight)
        results.append({
            "model": model_name,
            "value": loadout.value,
            "cost": loadout.cost(),
            "items": ", ".join(item.name for item in loadout.items)}
        )
    df = pd.DataFrame(results)
    df.to_csv("results/weights.csv", index=False)

if __name__ == "__main__":
    main()