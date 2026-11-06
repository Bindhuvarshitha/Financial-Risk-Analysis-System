import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_transaction.csv")

plt.figure(figsize=(8,5))
plt.hist(df["amount"], bins=20)

plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")

plt.savefig("transaction_graph.png")
plt.show()