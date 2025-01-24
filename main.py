import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

from data_loader import load_data_from_yahoo
from features import calculate_rsi, calculate_macd
from strategy import generate_signals
from backtest import backtest_signals
from utils import plot_signals, plot_equity_curve

def main():
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    initial_capital = 100000.0
    
    df = load_data_from_yahoo(ticker, start_date, end_date)
    print(f"Data loaded for {ticker} from {start_date} to {end_date}. Rows: {len(df)}")
    
    df = calculate_rsi(df, period=14)
    df = calculate_macd(df, fastperiod=12, slowperiod=26, signalperiod=9)
    
    df = generate_signals(df, rsi_lower=30, rsi_upper=70)
    
    result_df = backtest_signals(df, initial_capital=initial_capital)
    
    plot_signals(result_df, ticker)
    plot_equity_curve(result_df)

if __name__ == "__main__":
    main()