import pandas as pd
import time
from item import Item
from item_loader import load_items
from pulp_algorithm import PulpAlgorithm
from greedy_algorithm import GreedyAlgorithm
from brute_algorithm import BruteAlgorithm

def run_experiment(items, constraints, weights, dataset_size, results, reps):
    algorithms = {"PuLP": PulpAlgorithm(), "Greedy": GreedyAlgorithm(), "BruteForce": BruteAlgorithm()}
    for name, algorithm in algorithms.items():
        for run in range(reps):
            start = time.perf_counter()
            algorithm.optimise(items, constraints, weights)
            end = time.perf_counter()
            duration = end - start
            results.append({
                "algorithm": name,
                "dataset_size": dataset_size,
                "run": run + 1,
                "duration": duration
            })

    return results

def main():
    datasets = {
        8: [Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary"), Item("Judge",1850,0.7,0.4,0.5,0.15,"primary"),
            Item("Sheriff",800,0.55,0.05,0.05,0.7,"secondary"), Item("Shorty",300,0.4,0.15,0.2,0.35,"secondary"), 
            Item("Heavy Shields",1000,0.2,1,0.2,0.95,"shield"), Item("Light Shields",400,0.1,0.65,0.05,0.7,"shield"), 
            Item("Paranoia",250,0.5,0.7,0.85,0.7,"ability2"), Item("Dark Cover",150,0.15,0.9,0.95,0.9,"ability3")],

        11: [Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary"), Item("Guardian",2250,0.8,0.15,0.15,0.75,"primary"), Item("Stinger",1100,0.6,0.3,0.35,0.2,"primary"), Item("Judge",1850,0.7,0.4,0.5,0.15,"primary"),
            Item("Sheriff",800,0.55,0.05,0.05,0.7,"secondary"), Item("Shorty",300,0.4,0.15,0.2,0.35,"secondary"), 
            Item("Heavy Shields",1000,0.2,1,0.2,0.95,"shield"), Item("Light Shields",400,0.1,0.65,0.05,0.7,"shield"), 
            Item("Shrouded Step",100,0.2,0.6,0.45,0.65,"ability1"), Item("Paranoia",250,0.5,0.7,0.85,0.7,"ability2"), Item("Dark Cover",150,0.15,0.9,0.95,0.9,"ability3")],

        14: [Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary"), Item("Guardian",2250,0.8,0.15,0.15,0.75,"primary"), Item("Stinger",1100,0.6,0.3,0.35,0.2,"primary"), 
            Item("Odin",3200,0.95,0.25,0.5,0.8,"primary"), Item("Judge",1850,0.7,0.4,0.5,0.15,"primary"), Item("Bucky",850,0.5,0.3,0.3,0.1,"primary"),
            Item("Sheriff",800,0.55,0.05,0.05,0.7,"secondary"), Item("Ghost",500,0.45,0.1,0.05,0.55,"secondary"), Item("Shorty",300,0.4,0.15,0.2,0.35,"secondary"), 
            Item("Heavy Shields",1000,0.2,1,0.2,0.95,"shield"), Item("Light Shields",400,0.1,0.65,0.05,0.7,"shield"), 
            Item("Shrouded Step",100,0.2,0.6,0.45,0.65,"ability1"), Item("Paranoia",250,0.5,0.7,0.85,0.7,"ability2"), Item("Dark Cover",150,0.15,0.9,0.95,0.9,"ability3")],

        17: [Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary"), Item("Guardian",2250,0.8,0.15,0.15,0.75,"primary"), Item("Stinger",1100,0.6,0.3,0.35,0.2,"primary"), Item("Ares",1600,0.7,0.2,0.4,0.5,"primary"),
            Item("Odin",3200,0.95,0.25,0.5,0.8,"primary"), Item("Judge",1850,0.7,0.4,0.5,0.15,"primary"), Item("Bucky",850,0.5,0.3,0.3,0.1,"primary"), Item("Operator",4700,1,0.2,0.5,0.3,"primary"),
            Item("Classic",0,0.3,0.15,0.15,0.6,"secondary"), Item("Sheriff",800,0.55,0.05,0.05,0.7,"secondary"), Item("Ghost",500,0.45,0.1,0.05,0.55,"secondary"), Item("Shorty",300,0.4,0.15,0.2,0.35,"secondary"), 
            Item("Heavy Shields",1000,0.2,1,0.2,0.95,"shield"), Item("Light Shields",400,0.1,0.65,0.05,0.7,"shield"), 
            Item("Shrouded Step",100,0.2,0.6,0.45,0.65,"ability1"), Item("Paranoia",250,0.5,0.7,0.85,0.7,"ability2"), Item("Dark Cover",150,0.15,0.9,0.95,0.9,"ability3")],

        20: [Item("Vandal",2900,0.9,0.25,0.2,0.95,"primary"), Item("Guardian",2250,0.8,0.15,0.15,0.75,"primary"), Item("Spectre",1600,0.65,0.35,0.3,0.45,"primary"), 
            Item("Stinger",1100,0.6,0.3,0.35,0.2,"primary"), Item("Odin",3200,0.95,0.25,0.5,0.8,"primary"), Item("Ares",1600,0.7,0.2,0.4,0.5,"primary"), 
            Item("Judge",1850,0.7,0.4,0.5,0.15,"primary"), Item("Bucky",850,0.5,0.3,0.3,0.1,"primary"), Item("Operator",4700,1,0.2,0.5,0.3,"primary"),
            Item("Marshal",950,0.6,0.1,0.25,0.1,"primary"), 
            Item("Classic",0,0.3,0.15,0.15,0.6,"secondary"), Item("Sheriff",800,0.55,0.05,0.05,0.7,"secondary"), Item("Ghost",500,0.45,0.1,0.05,0.55,"secondary"), 
            Item("Frenzy",450,0.35,0.15,0.05,0.15,"secondary"), Item("Shorty",300,0.4,0.15,0.2,0.35,"secondary"), 
            Item("Heavy Shields",1000,0.2,1,0.2,0.95,"shield"), Item("Light Shields",400,0.1,0.65,0.05,0.7,"shield"), 
            Item("Shrouded Step",100,0.2,0.6,0.45,0.65,"ability1"), Item("Paranoia",250,0.5,0.7,0.85,0.7,"ability2"), Item("Dark Cover",150,0.15,0.9,0.95,0.9,"ability3")]
    }
    constraints = {
            "budget": 5500,
            "primary": 1,
            "secondary": 1,
            "shield": 1,
            "ability1": 2,
            "ability2": 1,
            "ability3": 1
        }
    weights = {"offensive": 0.3, "defensive": 0.3, "utility": 0.2, "versatility": 0.2}
    results = []
    for dataset_size, items in datasets.items():
        results = run_experiment(items, constraints, weights, dataset_size, results, reps=10)

    df = pd.DataFrame(results)
    df.to_csv("results/performance.csv", index=False)

if __name__ == "__main__":
    main()