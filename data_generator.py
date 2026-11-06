import pandas as pd
import random
from datetime import datetime, timedelta

data = []

for i in range(1, 5001):
    data.append([
        f"TXN_{i}",
        f"USER_{random.randint(1000,9999)}",
        random.randint(100, 50000),
        random.choice(["Credit", "Debit", "UPI", "Bank Transfer"]),
        random.choice(["ATM", "Branch", "Online"]),
        random.choice(["Mumbai", "London", "Tokyo", "New York", "Sydney"])
    ])

df = pd.DataFrame(data, columns=[
    "Transaction_ID",
    "Account_ID",
    "amount",
    "Transaction_Type",
    "channel",
    "region"
])

df.to_csv("clean_transaction.csv", index=False)

print("5000 records generated")
