class Loadout:
    def __init__(self, items):
        self.items = items

    def cost(self):
        return sum(item.cost for item in self.items)

    def value(self):
        return sum(item.value for item in self.items)