# Financial Risk Analysis System

A simple Flask application for reviewing transaction data and highlighting potentially high-risk transactions.

## Features

- Displays transaction totals and average transaction amount
- Shows the minimum and maximum transaction amounts
- Lists transactions above the risk threshold of 20,000
- Includes pages for analysis, alerts, graphs, and project information

## Requirements

- Python 3
- Packages listed in `requirements.txt`

## Setup and Run

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Make sure `clean_transaction.csv` is in the project root.

3. Start the application:

   ```bash
   python app.py
   ```

4. Open the local URL shown in the terminal (usually `http://127.0.0.1:5000`).

## Project Structure

- `app.py` — Flask application and dashboard routes
- `clean_transaction.csv` — transaction data used by the application
- `templates/` — HTML page templates
- `static/` — static assets
- `requirements.txt` — Python dependencies
