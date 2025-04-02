def backtest_moving_average_strategy(df, initial_cash=100000, position_pct=0.1, stop_loss_pct=0.05):
    df = df.copy()
    cash = initial_cash
    shares = 0
    buy_price = 0
    portfolio_values = []

    for date, row in df.iterrows():
        price = row['Close']
        signal = row['Position']

        # === Stop-loss check ===
        if shares > 0 and price < buy_price * (1 - stop_loss_pct):
            cash += shares * price
            shares = 0

        # === Buy signal ===
        if signal == 1 and cash > 0:
            allocation = initial_cash * position_pct
            num_shares = allocation // price
            if num_shares > 0:
                shares += num_shares
                cash -= num_shares * price
                buy_price = price

        # === Sell signal ===
        elif signal == -1 and shares > 0:
            cash += shares * price
            shares = 0

        portfolio_value = cash + (shares * price)
        portfolio_values.append(portfolio_value)

    df['Portfolio Value'] = portfolio_values
    return df
