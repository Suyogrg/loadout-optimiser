from optimiser import Optimiser
from loadout import Loadout
from value import calculate
from validation import is_valid

class GreedyAlgorithm(Optimiser):
    def optimise(self, items, constraints, weights):
        sorted_items = sorted(items,
            key=lambda item: (
                calculate(item, weights) / item.cost
                if item.cost > 0
                else calculate(item, weights)
            ),
            reverse=True
        )
        selected = []
        total_value = 0
        for item in sorted_items:
            if is_valid(selected + [item], constraints):
                selected.append(item)
                total_value += calculate(item, weights)

        return Loadout(selected, total_value)