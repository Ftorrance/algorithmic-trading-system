import pandas as pd
import matplotlib.pyplot as plt
from data.collect_data import download_data
from strategies.moving_average import moving_average_crossover
from backtest.backtester import backtest_moving_average_strategy
from backtest.performance import calculate_performance

# === Step 1: Download historical data ===
ticker = "AAPL"
start_date = "2023-01-01"
end_date = "2023-12-31"
download_data(ticker, start=start_date, end=end_date)

# === Step 2: Load and clean the CSV ===
df = pd.read_csv(f"data/{ticker}.csv", skiprows=2)
df = df.rename(columns={df.columns[0]: "Date"})
df["Date"] = pd.to_datetime(df["Date"], utc=True)
df.set_index("Date", inplace=True)
df = df.iloc[:, :5]  # Use only first 5 columns
df.columns = ["Close", "High", "Low", "Open", "Volume"]

# === Step 3: Apply Moving Average Crossover strategy ===
df = moving_average_crossover(df)

# === Step 4: Backtest strategy with risk management ===
df = backtest_moving_average_strategy(
    df,
    initial_cash=100000,
    position_pct=0.1,      # invest 10% per trade
    stop_loss_pct=0.05     # sell if -5% below buy price
)

# === Step 5: Calculate performance metrics ===
df, sharpe_ratio, max_drawdown = calculate_performance(df)

# === Step 6: Plot 4-panel performance dashboard ===
fig, axes = plt.subplots(2, 2, figsize=(20, 10))
fig.suptitle(f"{ticker} - Strategy Analysis Dashboard", fontsize=16)

# Chart 1: Close Price
axes[0, 0].plot(df['Close'], label="Close Price", linewidth=1.5)
axes[0, 0].set_title("Stock Price")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Price ($)")
axes[0, 0].legend()
axes[0, 0].grid(True)

# Chart 2: Strategy Signals
axes[0, 1].plot(df['Close'], label='Close Price', alpha=0.6)
axes[0, 1].plot(df['SMA_Short'], label='Short MA (20)', linewidth=1.2)
axes[0, 1].plot(df['SMA_Long'], label='Long MA (50)', linewidth=1.2)
axes[0, 1].plot(df[df['Position'] == 1].index,
                df['Close'][df['Position'] == 1],
                '^', color='green', label='Buy Signal', markersize=10)
axes[0, 1].plot(df[df['Position'] == -1].index,
                df['Close'][df['Position'] == -1],
                'v', color='red', label='Sell Signal', markersize=10)
axes[0, 1].set_title("Strategy Buy/Sell Signals")
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Price ($)")
axes[0, 1].legend()
axes[0, 1].grid(True)

# Chart 3: Portfolio Value
axes[1, 0].plot(df.index, df['Portfolio Value'], label="Portfolio Value", color="purple")
axes[1, 0].set_title("Portfolio Value Over Time")
axes[1, 0].set_xlabel("Date")
axes[1, 0].set_ylabel("Value ($)")
axes[1, 0].legend()
axes[1, 0].grid(True)

# Chart 4: Performance Metrics with two Y-axes
ax1 = axes[1, 1]
ax2 = ax1.twinx()

ax1.plot(df.index, df['Cumulative Return'], label="Cumulative Return", color="blue")
ax2.plot(df.index, df['Drawdown'], label="Drawdown", color="red")

ax1.set_title("Performance Metrics")
ax1.set_xlabel("Date")
ax1.set_ylabel("Cumulative Return", color="blue")
ax2.set_ylabel("Drawdown", color="red")

# Fix legend manually
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

ax1.grid(True)


plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# === Step 7: Print Performance Stats ===
print(f"\n📈 Final Portfolio Value: ${df['Portfolio Value'].iloc[-1]:,.2f}")
print(f"📊 Total Return: {(df['Cumulative Return'].iloc[-1] - 1) * 100:.2f}%")
print(f"📉 Max Drawdown: {max_drawdown:.2%}")
print(f"⚖️ Sharpe Ratio: {sharpe_ratio:.2f}")
