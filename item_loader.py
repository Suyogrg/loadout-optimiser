import json
from item import Item

def load_items():
    with open("items.json", "r") as file:
        data = json.load(file)

    items = []
    for item_data in data:
        item = Item(
            name=item_data["name"],
            cost=item_data["cost"],
            offensive=item_data["offensive"],
            defensive=item_data["defensive"],
            utility=item_data["utility"],
            versatility=item_data["versatility"],
            group=item_data["group"],
            slots=item_data.get("slots"),
            agent=item_data.get("agent")
        )
        items.append(item)
    return items

def get_items(items, credits, selected_agent):
    filtered_items = []

    for item in items:
        if item.agent == selected_agent or item.agent == None:
            if item.cost <= credits:
                filtered_items.append(item)

    return filtered_items