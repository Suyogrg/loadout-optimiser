import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/quality.csv")
df["optimal"] = df.groupby("budget")["value"].transform("max")
df["optimality_gap"] = ((df["optimal"] - df["value"]) / df["optimal"]) * 100
df = df.pivot(index="budget", columns="algorithm", values="optimality_gap")
df.plot(kind="line", marker="o")
plt.title("Optimality Gap Across Budgets")
plt.xlabel("Budget")
plt.ylabel("Optimality Gap (%)")
plt.grid()
plt.savefig("results/optimality_gap.png")
plt.show()