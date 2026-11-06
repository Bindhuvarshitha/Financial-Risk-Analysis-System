import pandas as pd

df = pd.read_csv("clean_transaction.csv")

print("Missing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())