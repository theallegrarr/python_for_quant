# lists
prices = [10, 12, 13, 18, 14]

print(prices[0])
print(prices[-1])

prices.append(16)
print(prices)

# tuples
trade = ("AAPL", 100, 182.45)
ticker, quantity, price = trade

print(ticker)

# dictionaries
portfolio = {
    "AAPL": 150,
    "MSFT": 80,
    "NVDA": 40
}

print(portfolio["AAPL"])
portfolio["AAPL"] += 25

print(portfolio)


# sets
symbols = ["AAPL", "MSFT", "AAPL", "NVDA", "MSFT"]
uniqye_symbols = set(symbols)
print(uniqye_symbols)

#control flow
price = 104

if price > 100:
    print("Expensive stock")
else:
    print("Affordable stock")

# Loops
for price in prices:
    print(price)

# functions
def simple_return(start, end):
    return(end - start)/start

r = simple_return(100, 105)
print(r)

# imports
import math

volatility = math.sqrt(0.04)
print(volatility)
