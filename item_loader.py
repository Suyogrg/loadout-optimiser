import json

def load_items():
    with open("items.json", "r") as file:
        data = json.load(file)

    return data

def get_items(items, credits, selected_agent):
    filtered_items = []

    for item in items:
        if item.get("agent") == selected_agent or item.get("agent") == None:
            if item.get("cost") <= credits:
                filtered_items.append(item)

    return filtered_items