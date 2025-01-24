import yfinance as yf
import pandas as pd

def load_data_from_yahoo(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Loads historical data from Yahoo Finance for the specified ticker and date range.

    :param ticker: Stock ticker symbol, e.g., "AAPL".
    :param start_date: Start dpyate in 'YYYY-MM-DD' format.
    :param end_date: End date in 'YYYY-MM-DD' format.
    :return: DataFrame with OHLC data plus Adj Close and Volume.
    """
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    df.rename(columns={
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'adj_close',
        'Volume': 'volume'
    }, inplace=True)

    df.dropna(inplace=True)
    return df