import numpy as np

prices = [101.2, 102.5, 103.1, 100.8]

np_prices = np.array(prices)

print(f"shape: {np_prices.shape}")
print(f"data type: {np_prices.dtype}")
print(f"axis: {np_prices.ndim}")

fundamentals = np.array([
#   [P/E,   ROE, DebtEquity]
    [15.2, 0.18, 0.4],
    [12.2, 0.14, 0.2],
    [21.2, 0.17, 0.9],
])

print(f"shape: {fundamentals.shape}")
print(f"all ticker Price to Earning Ratios: {fundamentals[:, 0]}")
print(f"First row of the array: {fundamentals[0, :]}")

# 3D Array
fundamentals_3d = np.array([
    [ 
#       [P/E,   ROE, DebtEquity]
        [15.2, 0.18, 0.4],
        [12.2, 0.14, 0.2],
        [21.2, 0.17, 0.9],
    ],
    [   
#       [P/E,   ROE, DebtEquity]
        [25.2, 0.32, 0.8],
        [32.2, 0.12, 0.11],
        [41.2, 0.17, 0.9],
    ]
])

print(f"shape: {fundamentals_3d.shape}")
print(f"first array, second row, first column: {fundamentals_3d[0, 1, 0]}")
print(f"sliced: {fundamentals_3d[:, :, 0]}")

# calculating the mean with numpy
average_price_to_earnings = fundamentals_3d[:, :, 0].mean(axis=0)

print(average_price_to_earnings)


# vectorization
# for i in range(1, len(prices))...
returns = np_prices[1:] / np_prices[:-1] - 1

# [101.2, 102.5, 103.1, 100.8]
print(returns)



# Broadcasting
pe = fundamentals[:, 0]
cheap = pe < 20

print(fundamentals[cheap])
#   [15.2], True
#   [12.2], True
#   [21.2], False
print(cheap)





