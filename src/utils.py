import matplotlib.pyplot as plt

def plot_signals(df, ticker: str):
    """
    Plot the close price along with buy/sell signals.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['close'], label='Close Price', color='blue')
    
    buy_signals = df[df['signal'] == 1]
    sell_signals = df[df['signal'] == -1]
    
    plt.scatter(buy_signals.index, buy_signals['close'], marker='^', color='green', label='Buy Signal', alpha=0.8)
    plt.scatter(sell_signals.index, sell_signals['close'], marker='v', color='red', label='Sell Signal', alpha=0.8)
    
    plt.title(f"{ticker} Price & Trading Signals")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def plot_equity_curve(df):
    """
    Plot the strategy equity curve over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['strategy_equity'], label='Strategy Equity', color='purple')
    
    plt.title("Strategy Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.legend()
    plt.show()