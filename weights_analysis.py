import pandas as pd
import matplotlib.pyplot as plt

def categorise_items(item_string):
    items = [item.strip() for item in item_string.split(",")]

    return pd.Series({
        "Primary": items[0],
        "Secondary": items[1],
        "Shield": items[2],
        "Abilities": ", ".join(items[3:])
    })

df = pd.read_csv("results/weights.csv")
categories = df["items"].apply(categorise_items)
table = pd.concat(
    [df[["model", "value", "cost"]], categories],
    axis=1
)

print(table)