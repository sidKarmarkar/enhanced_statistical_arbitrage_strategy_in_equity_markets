import pandas as pd

def generate_signals(df: pd.DataFrame, 
                     rsi_lower: float = 30, 
                     rsi_upper: float = 70) -> pd.DataFrame:
    """
    Generates trading signals based on a dual strategy approach combining:
    - Momentum (MACD crossovers)
    - Mean reversion (RSI oversold/overbought)

    :param df: DataFrame with 'rsi', 'macd_line', 'macd_signal' columns.
    :param rsi_lower: RSI oversold threshold.
    :param rsi_upper: RSI overbought threshold.
    :return: DataFrame with new 'signal' column (1 = long, -1 = short, 0 = flat).
    """
    df['signal'] = 0
    
    df.loc[df['macd_line'] > df['macd_signal'], 'signal'] = 1
    df.loc[df['macd_line'] < df['macd_signal'], 'signal'] = -1
    
    df.loc[df['rsi'] < rsi_lower, 'signal'] = 1
    
    df.loc[df['rsi'] > rsi_upper, 'signal'] = -1
    return df