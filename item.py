class Item:
    def __init__(
        self,
        name,
        cost,
        offensive,
        defensive,
        utility,
        versatility,
        group,
        slots=None,
        agent=None
    ):
        self.name = name
        self.cost = cost
        self.offensive = offensive
        self.defensive = defensive
        self.utility = utility
        self.versatility = versatility
        self.group = group
        self.slots = slots
        self.agent = agent