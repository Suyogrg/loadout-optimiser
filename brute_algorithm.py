from optimiser import Optimiser
from loadout import Loadout
from value import calculate
from validation import is_valid

class BruteAlgorithm(Optimiser):
    def optimise(self, items, constraints, weights):

        def search(i, current):
            if i == len(items):
                if is_valid(current, constraints):
                    value = sum(calculate(item, weights) for item in current)
                    return current, value
                return [], 0

            exclude_item, exclude_value = search(i+1, current)
            include_item, include_value = search(i+1, current + [items[i]])

            if include_value > exclude_value:
                return include_item, include_value
            else:
                return exclude_item, exclude_value

        selected, total_value = search(0, [])

        return Loadout(selected, total_value)