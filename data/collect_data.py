import yfinance as yf
import os

def download_data(ticker, start, end):
    # Explicitly call .history() to get correct structure
    stock = yf.Ticker(ticker)
    data = stock.history(start=start, end=end, auto_adjust=False)

    # Clean up column names
    data = data.rename(columns={
        "Open": "Open",
        "High": "High",
        "Low": "Low",
        "Close": "Close",
        "Volume": "Volume",
        "Adj Close": "Adj Close"
    })

    # Save to CSV with proper index label
    if not os.path.exists("data"):
        os.makedirs("data")

    data.to_csv(f"data/{ticker}.csv", index_label="Date")
    print(f"✅ Data saved to data/{ticker}.csv")
