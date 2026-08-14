from abc import ABC, abstractmethod

class Optimiser(ABC):
    @abstractmethod
    def optimise(self, items, budget, weights):
        pass