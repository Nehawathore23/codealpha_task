import csv

print("📈 Welcome to Stock Portfolio Tracker\n")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}
print("📌 Available Stocks:")
for stock, price in stock_prices.items():
    print(f"   {stock} → ${price}")
print()
portfolio = {}
total_investment = 0

def calculate_stock_value(stock, quantity):
    if stock in stock_prices:
        return stock_prices[stock] * quantity
    else:
        print(f"❌ Stock '{stock}' not found in database!")
        return 0

def save_portfolio_csv(filename, portfolio, total):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Symbol", "Quantity", "Price", "Total Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            writer.writerow([stock, qty, price, price*qty])
        writer.writerow([])
        writer.writerow(["", "", "Total Investment", total])
    print(f"📁 Portfolio saved to '{filename}'\n")

while True:
    stock = input("Enter stock symbol (or 'STOP' to finish): ").upper()
    if stock == "STOP":
        break
    quantity_input = input(f"Enter quantity of {stock}: ")
    if not quantity_input.isdigit():
        print("❌ Invalid quantity! Please enter a number.\n")
        continue
    quantity = int(quantity_input)

    value = calculate_stock_value(stock, quantity)
    if value > 0:
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity
        total_investment += value
        print(f"Added: {stock} x {quantity} = ${value}\n")

print("\n----- Portfolio Summary -----")
for s, q in portfolio.items():
    print(f"{s}: {q} shares → ${stock_prices[s]*q}")
print("-------------------------------")
print(f"💰 Total Investment Value = ${total_investment}\n")

save = input("Do you want to save the portfolio to a CSV file? (yes/no): ").lower()
if save == "yes":
    save_portfolio_csv("portfolio.csv", portfolio, total_investment)

print("✅ Thank you for using Stock Portfolio Tracker!")
