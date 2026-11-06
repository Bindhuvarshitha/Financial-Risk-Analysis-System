from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("clean_transaction.csv")


@app.route("/")
def home():
    total = len(df)
    high_risk = len(df[df["amount"] > 20000])
    avg_amount = round(df["amount"].mean(), 2)

    return render_template(
        "index.html",
        total=total,
        high_risk=high_risk,
        avg_amount=avg_amount
    )


@app.route("/analysis")
def analysis():
    total = len(df)
    maximum = df["amount"].max()
    minimum = df["amount"].min()

    return render_template(
        "analysis.html",
        total=total,
        maximum=maximum,
        minimum=minimum
    )


@app.route("/alerts")
def alerts():
    alerts_data = df[df["amount"] > 20000]

    return render_template(
        "alerts.html",
        tables=[alerts_data.to_html(index=False)]
    )


@app.route("/graphs")
def graphs():
    return render_template("graphs.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)