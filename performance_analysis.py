import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/performance.csv")
df = (df.groupby(["algorithm", "dataset_size"]).agg(
    mean_time = ("duration", "mean"), 
    std_time=("duration", "std")
    ).reset_index())
print(df)
for algorithm, group in df.groupby("algorithm"):
    plt.plot(group["dataset_size"], group["mean_time"], marker="o", label=algorithm)
plt.title("Algorithm Execution Time Over Increasing Number of Items")
plt.xlabel("Number of items")
plt.ylabel("Mean time (s)")
plt.legend()
plt.savefig("results/runtime_performance.png")
plt.show()