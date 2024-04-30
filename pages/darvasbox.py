import pandas as pd
import yfinance as yf
import matplotlib
matplotlib.use('Agg')  # This sets the Tkinter backend which supports windowed output
import matplotlib.pyplot as plt
import mplfinance as mpf
import talib

from datetime import datetime

def fetch_data(stock_symbol, start_date, end_date):
    """Fetch historical stock data using yfinance."""
    df = yf.download(stock_symbol, start=start_date, end=end_date)
    return df

import pandas as pd

# Load your data
data = pd.read_csv('your_data.csv', index_col='Date', parse_dates=True)

# Calculate Darvas Box
data['upper'], data['lower'] = talib.MINMAX(data['Close'], timeperiod=14)

# Identify candlestick pattern (e.g., Bullish Engulfing)
data['candle_pattern'] = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

# Filter for significant candlestick patterns
data['pattern_signal'] = data['candle_pattern'].apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))

# Volume (Simple check if current volume is higher than the average of the past 10 days)
data['volume_avg'] = data['Volume'].rolling(window=10).mean()
data['volume_signal'] = data['Volume'] > data['volume_avg']

# Combine signals
data['signal'] = data.apply(lambda row: 1 if row['Close'] > row['upper'] and row['volume_signal'] and row['pattern_signal'] == 1 else (-1 if row['Close'] < row['lower'] and row['volume_signal'] and row['pattern_signal'] == -1 else 0), axis=1)

# Plotting with mplfinance
ap = [mpf.make_addplot(data['upper']), mpf.make_addplot(data['lower']), mpf.make_addplot(data['signal'], type='scatter', markersize=200, marker='^')]
mpf.plot(data, type='candle', addplot=ap, volume=True, style='yahoo')

