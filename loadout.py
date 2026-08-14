class Loadout:
    def __init__(self, items, value):
        self.items = items
        self.value = value

    def cost(self):
        return sum(item.cost for item in self.items)