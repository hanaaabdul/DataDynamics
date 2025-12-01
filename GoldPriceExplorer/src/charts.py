import matplotlib.pyplot as plt

def plot_price(df):
    plt.figure(figsize=(10,4))
    plt.plot(df.index, df['price'], label="Gold Price")
    plt.title("Gold Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_moving_average(df, window=30):
    ma = df['price'].rolling(window).mean()
    plt.figure(figsize=(10,4))
    plt.plot(df.index, df['price'], label="Price")
    plt.plot(df.index, ma, label=f"MA{window}")
    plt.legend()
    plt.tight_layout()
    plt.show()
