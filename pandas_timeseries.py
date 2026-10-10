import pandas as pd

prices = pd.DataFrame(
          {"close": [101.2, 102.5, 103.1, 101.2, 103.0]},
    index=[
        "2026-08-20 09:30",
        "2026-08-20 10:00",
        "2026-08-20 10:30",
        "2026-08-20 11:00",
        "2026-08-20 11:30",
    ]
)

print("Index dtype: ", prices.index.dtype)

# Converting the string index into DateTimeIndex
prices.index = pd.to_datetime(prices.index)
print("Index dtype after: ", prices.index.dtype)
print("First index timestamp: ", prices.index[0])


# Slicing by time range
window = prices.loc["2026-08-20 10:00":"2026-08-20 11:30"]
full_day_prices = prices.loc["2026-08-20"]

print("prices from 10 am to 11:30 am", window)
print("full day prices", full_day_prices)


# resample vs asfreq
hourly_resampled = prices["close"].resample("1h").last()
hourly_asfreq = prices["close"].asfreq("1h")

print(hourly_resampled)
print(hourly_asfreq)


# rolling vs ever-growing expanding window
prices["sma_3"] = prices["close"].rolling(3).mean()
prices["expanding_mean"] = prices["close"].expanding().mean()

print("-----------------------------")
print(prices[["close", "sma_3", "expanding_mean"]])


# shift
prices["signal"] = prices["close"] > prices["sma_3"]
prices["decision"] = prices["signal"].shift(1)

print("-----------------------------")
print(prices[["close", "sma_3", "signal", "decision"]])


# Filling gaps
gappy = prices["close"].copy()
gappy.iloc[2] = None

print("-----------------------------")
print(gappy.ffill())
print(gappy.bfill())


# Strategy pattern
session = prices.loc["2026-08-20 09:30":"2026-08-20 12:30"]
session["sma_3"] = session["close"].rolling(3).mean()
session["signal"] = session["close"] > session["sma_3"]
session["decision"] = session["signal"].shift(1)

print("-----------------------------")
print(session[["close", "sma_3", "signal", "decision"]])

































