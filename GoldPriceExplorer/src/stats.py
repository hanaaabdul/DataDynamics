def compute_basic_stats(df):
    mean_price = df['price'].mean()
    max_price = df['price'].max()
    min_price = df['price'].min()
    volatility = df['price'].pct_change().std()
    return mean_price, max_price, min_price, volatility

