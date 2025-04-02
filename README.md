# 📈 Algorithmic Trading System (Moving Average Crossover)

This project implements a complete algorithmic trading strategy using Python. It simulates buying and selling based on moving average crossovers, with risk management and performance analysis built in.

---

## 🚀 Features

- ✅ Data collection from Yahoo Finance (via `yfinance`)
- 📊 Strategy: **Moving Average Crossover (SMA 20 vs SMA 50)**
- 💰 Backtesting with:
  - Position sizing (10% capital per trade)
  - Stop-loss (5% below entry price)
- 📈 Portfolio value and trade simulation
- 📉 Performance metrics:
  - Cumulative return
  - Max drawdown
  - Sharpe ratio
- 📺 4-panel dashboard with:
  - Stock price
  - Buy/sell signals
  - Portfolio value
  - Return & drawdown analysis

---

## 🧰 Tech Stack

- Python 3.x
- `pandas`
- `matplotlib`
- `yfinance`
- `numpy`

---

## 🛠️ Installation

Clone the repo:

```bash
git clone https://github.com/Ftorrance/algorithmic-trading-system.git
cd algorithmic-trading-system
