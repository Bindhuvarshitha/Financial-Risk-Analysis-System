import pandas as pd

df = pd.read_csv("clean_transaction.csv")

print("Total Transactions:", len(df))
print("Average Amount:", df["amount"].mean())
print("Maximum Amount:", df["amount"].max())
print("Minimum Amount:", df["amount"].min())

print("\nTransaction Types")
print(df["Transaction_Type"].value_counts())

print("\nRegions")
print(df["region"].value_counts())