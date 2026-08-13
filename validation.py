def is_valid(selection, constraints):
    cost = 0
    counts = {
        "primary": 0,
        "secondary": 0,
        "shield": 0,
        "ability1": 0,
        "ability2": 0,
        "ability3": 0
    }
    for item in selection:
        cost += item.cost
        counts[item.group] += 1

    valid = (cost <= constraints["budget"] and
            counts["primary"] <= constraints["primary"] and
            counts["secondary"] <= constraints["secondary"] and
            counts["shield"] <= constraints["shield"] and
            counts["ability1"] <= constraints["ability1"] and
            counts["ability2"] <= constraints["ability2"] and
            counts["ability3"] <= constraints["ability3"])
    
    return valid