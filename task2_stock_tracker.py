# Hardcoded stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 120,
    "MSFT": 300
}

portfolio = {}
total_value = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Invalid stock! Try again.")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total investment
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares × {stock_prices[stock]} = {value}")

print("\nTotal Investment Value:", total_value)

# (Optional) Save to file
with open("portfolio.txt", "w") as f:
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares × {stock_prices[stock]} = {qty * stock_prices[stock]}\n")
    f.write(f"\nTotal Investment Value: {total_value}")
