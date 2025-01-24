import pandas as pd

def calculate_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """
    Calculates the RSI (Relative Strength Index) on the close price.

    :param df: DataFrame containing at least a 'close' column.
    :param period: Lookback period for RSI calculation.
    :return: DataFrame with additional 'rsi' column.
    """
    delta = df['close'].diff()
    
    gains = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    losses = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gains / losses
    df['rsi'] = 100 - (100 / (1 + rs))
    
    return df

def calculate_macd(df: pd.DataFrame, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9) -> pd.DataFrame:
    """
    Calculates the MACD (Moving Average Convergence Divergence) for momentum analysis.

    :param df: DataFrame containing at least a 'close' column.
    :param fastperiod: Fast EMA period.
    :param slowperiod: Slow EMA period.
    :param signalperiod: Signal line EMA period.
    :return: DataFrame with additional 'macd_line' and 'macd_signal' columns.
    """
    df['ema_fast'] = df['close'].ewm(span=fastperiod, adjust=False).mean()
    df['ema_slow'] = df['close'].ewm(span=slowperiod, adjust=False).mean()
    
    df['macd_line'] = df['ema_fast'] - df['ema_slow']
    df['macd_signal'] = df['macd_line'].ewm(span=signalperiod, adjust=False).mean()
    
    return df