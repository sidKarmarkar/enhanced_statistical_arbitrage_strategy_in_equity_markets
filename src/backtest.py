import pandas as pd
import numpy as np

def backtest_signals(df: pd.DataFrame, initial_capital: float = 100000.0) -> pd.DataFrame:
    """
    Simple backtest of the generated signals:
    - Buys (or sells short) 1 unit for each positive (or negative) signal
    - Tracks PnL and calculates daily returns
    - Returns performance metrics and equity curve

    :param df: DataFrame with 'close' and 'signal' columns.
    :param initial_capital: Starting capital for the strategy.
    :return: DataFrame with 'strategy_equity' and 'strategy_returns' columns.
    """
    df = df.copy()  
    df['position'] = df['signal'].shift(1).fillna(0)
    
    df['market_return'] = df['close'].pct_change()
    
    df['strategy_return'] = df['position'] * df['market_return']
    
    df['strategy_equity'] = (1 + df['strategy_return']).cumprod() * initial_capital
    
    df['daily_pct_change'] = df['strategy_equity'].pct_change()
    
    daily_mean = df['daily_pct_change'].mean()
    daily_std = df['daily_pct_change'].std()
    annual_sharpe = (daily_mean / (daily_std + 1e-9)) * np.sqrt(252)
    total_return = (df['strategy_equity'].iloc[-1] / df['strategy_equity'].iloc[0]) - 1
    
    print("=== Backtest Summary ===")
    print(f"Initial Capital: {initial_capital}")
    print(f"Final Equity: {df['strategy_equity'].iloc[-1]:.2f}")
    print(f"Total Return: {total_return * 100:.2f}%")
    print(f"Annualized Sharpe Ratio: {annual_sharpe:.2f}")
    
    return df