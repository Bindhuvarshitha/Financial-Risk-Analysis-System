import pandas as pd

df = pd.read_csv("clean_transaction.csv")

def calculate_risk(amount):
    if amount > 20000:
        return "High Risk"
    elif amount > 10000:
        return "Medium Risk"
    else:
        return "Low Risk"

df["Risk"] = df["amount"].apply(calculate_risk)

alerts = df[df["Risk"] != "Low Risk"]

print(alerts.head())

alerts.to_csv("reports/fraud_alerts.csv", index=False)

print("Fraud alerts generated successfully!")