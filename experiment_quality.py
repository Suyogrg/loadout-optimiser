import time
import pandas as pd
from pulp_algorithm import PulpAlgorithm
from greedy_algorithm import GreedyAlgorithm
from brute_algorithm import BruteAlgorithm
from item_loader import load_items


def run_experiment(items, budget, weights, results):
    algorithms = {"PuLP": PulpAlgorithm(), "Greedy": GreedyAlgorithm(), "BruteForce": BruteAlgorithm()}
    for name, algorithm in algorithms.items():
        constraints = {
            "budget": budget,
            "primary": 1,
            "secondary": 1,
            "shield": 1,
            "ability1": 2,
            "ability2": 1,
            "ability3": 1
        }
        start = time.perf_counter()
        loadout = algorithm.optimise(items, constraints, weights)
        end = time.perf_counter()
        duration = end - start
        results.append({
            "budget": budget,
            "algorithm": name,
            "value": loadout.value,
            "cost": loadout.cost(),
            "count": len(loadout.items),
            "duration": duration
        })

    return results

def main():
    items = load_items()
    filtered = [item for item in items if item.agent == "Omen" or item.agent == None]
    weights = {"offensive": 0.3, "defensive": 0.3, "utility": 0.2, "versatility": 0.2}
    budgets = [1500,2500,3500,4500,5500]
    results = []
    for budget in budgets:
        results = run_experiment(filtered, budget, weights, results)
    df = pd.DataFrame(results)
    df.to_csv("results/quality.csv", index=False)
    print(df)

if __name__ == "__main__":
    main()