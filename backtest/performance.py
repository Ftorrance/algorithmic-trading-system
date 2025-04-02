import numpy as np
import pandas as pd

def calculate_performance(df, risk_free_rate=0.01):
    """
    Adds performance metrics to the DataFrame.
    """
    df = df.copy()
    
    # Daily returns
    df['Daily Return'] = df['Portfolio Value'].pct_change()

    # Cumulative returns
    df['Cumulative Return'] = (1 + df['Daily Return']).cumprod()

    # Max Drawdown
    df['Cumulative Max'] = df['Portfolio Value'].cummax()
    df['Drawdown'] = (df['Portfolio Value'] - df['Cumulative Max']) / df['Cumulative Max']

    # Sharpe Ratio (assumes 252 trading days)
    sharpe_ratio = (
        (df['Daily Return'].mean() - risk_free_rate / 252)
        / df['Daily Return'].std()
    ) * np.sqrt(252)

    return df, sharpe_ratio, df['Drawdown'].min()
