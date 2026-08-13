from optimiser import Optimiser
from loadout import Loadout
from value import calculate
import pulp

class PulpAlgorithm(Optimiser):
    def optimise(self, items, constraints, weights):

        prob = pulp.LpProblem("Loadout_Optimization", pulp.LpMaximize)
        x = {
            i: prob.add_variable(f"x_{i}", cat="Binary")
            for i in range(len(items))
        }
        prob += pulp.lpSum(calculate(items[i], weights) * x[i] for i in x)
        prob += pulp.lpSum(items[i].cost * x[i] for i in x) <= constraints["budget"]
        prob += pulp.lpSum(x[i] for i in x if items[i].group == "primary") <= constraints["primary"]
        prob += pulp.lpSum(x[i] for i in x if items[i].group == "secondary") <= constraints["secondary"]
        prob += pulp.lpSum(x[i] for i in x if items[i].group == "shield") <= constraints["shield"]
        prob += pulp.lpSum(x[i] for i in x if items[i].group == "ability1") <= constraints["ability1"]
        prob += pulp.lpSum(x[i] for i in x if items[i].group == "ability2") <= constraints["ability2"]
        prob += pulp.lpSum(x[i] for i in x if items[i].group == "ability3") <= constraints["ability3"]
        prob.solve()
        selected = [items[i] for i in x if pulp.value(x[i]) == 1]
        total_value = sum(calculate(item, weights) for item in selected)

        return Loadout(selected, total_value)