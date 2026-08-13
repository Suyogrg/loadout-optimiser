from pulp_algorithm import PulpAlgorithm

def get_agents(items):
    return sorted({item.agent for item in items if item.agent is not None})

def generate(items, agent, credits, weights):
    filtered = [item for item in items if item.agent == agent or item.agent == None]
    for item in filtered:
        if item.slots != None:
            if item.group == "ability1":
                ability1 = item.slots
            if item.group == "ability2":
                ability2 = item.slots
            if item.group == "ability2":
                ability3 = item.slots
    
    constraints = {
        "budget": credits,
        "primary": 1,
        "secondary": 1,
        "shield": 1,
        "ability1": ability1,
        "ability2": ability2,
        "ability3": ability3
        }
    
    optimiser = PulpAlgorithm()

    return optimiser.optimise(filtered,constraints,weights)