import yfinance as yf
import pandas as pd

def load_gold_data(years=5):
    df = yf.download("GC=F", period=f"{years}y")[["Adj Close"]]
    df = df.rename(columns={"Adj Close":"price"}).dropna()
    df.index.name = "date"
    return df
