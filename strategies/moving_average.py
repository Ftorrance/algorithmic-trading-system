import pandas as pd

def moving_average_crossover(data, short_window=20, long_window=50):
    """
    Add moving average signals to the DataFrame.
    """
    data['SMA_Short'] = data['Close'].rolling(window=short_window).mean()
    data['SMA_Long'] = data['Close'].rolling(window=long_window).mean()

    # Signal = 1 for Buy, 0 otherwise
    data['Signal'] = 0
    data.loc[data.index[short_window:], 'Signal'] = (
    data['SMA_Short'][short_window:] > data['SMA_Long'][short_window:]
).astype(int)


    # Position = +1 on Buy, -1 on Sell
    data['Position'] = data['Signal'].diff()

    return data
