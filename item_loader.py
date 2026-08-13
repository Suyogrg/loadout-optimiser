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
        if item.slots != None:
            for i in range(item.slots):
                items.append(item)
        else:
            items.append(item)

    return items