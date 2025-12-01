from src.load_data import load_gold_data
from src.stats import compute_basic_stats
from src.charts import plot_price, plot_moving_average

print("Loading data...")
df = load_gold_data()

print("Computing statistics...")
mean_price, max_price, min_price, vol = compute_basic_stats(df)

print("---- Gold Price Statistics (5-year period) ----")
print("Mean price:", round(mean_price, 2))
print("Max price:", round(max_price, 2))
print("Min price:", round(min_price, 2))
print("Volatility (std of % change):", round(vol, 4))

print("Generating charts...")
plot_price(df)
plot_moving_average(df)
