import numpy as np
import pandas as pd

prices_np = np.array([101.2, 102.5, 103.1])

prices_pd = pd.Series([101.2, 102.5, 103.1],
                index=["AAPL", "MSFT", "GOOG"])


pe_ratios = pd.Series(
          [15.2, 28.7, 11.0],
    index=["AAPL", "MSFT", "GOOG"],
    name="pe_ratio"
)

print(pe_ratios.values)
print("Labels: ", pe_ratios.index)
print("MSFT price to earnings ratio: ", pe_ratios["MSFT"])

# DataFrame
fundamentals = pd.DataFrame(
    {
        "pe": [15.2, 28.7, 11.0],
        "roe": [0.18, 0.09, 0.25],
        "de": [0.4, 1.2, 0.3],
    },
    index=["AAPL", "MSFT", "GOOG"],
)

print("Fundamentals shape: ", fundamentals.shape)
print("Fundamentals columns: ", fundamentals.columns)
print("Fundamentals index: ", fundamentals.index)
print("Fundamentals head: ", fundamentals.head())
print("Fundamentals row statistics: ", fundamentals.describe())

# Data selection
print("----------------")
print(fundamentals["pe"])
print("Multiple columns")
print(fundamentals[["pe", "roe"]])
print("Selecting data by label")
print(fundamentals.loc["AAPL"])
print("Selecting PE column by label")
print(fundamentals.loc["AAPL", "pe"])
print("Selecting data by integer location (iloc)")
print(fundamentals.iloc[0])
print("Specifying row and column by integer location (iloc)")
print(fundamentals.iloc[0, 0])


# Computed columns and vectorization
fundamentals["quality"] = fundamentals["roe"] / fundamentals["de"]
print("Computed quality result:")
print(fundamentals)

# Boolean masks
cheap = fundamentals["pe"] < 20
print("mask result: ", fundamentals[cheap])

screen = (fundamentals["pe"] < 20) & (fundamentals["roe"] > 0.15)
print("screen result: ", fundamentals[screen])

















