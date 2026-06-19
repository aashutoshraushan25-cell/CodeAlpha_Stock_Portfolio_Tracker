STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
}


def show_available_stocks():
    print("Available stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")


def get_quantity(symbol):
    while True:
        quantity_text = input(f"Enter quantity for {symbol}: ").strip()

        if not quantity_text.isdigit():
            print("Please enter a valid whole number.")
            continue

        quantity = int(quantity_text)
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        return quantity


def build_portfolio():
    portfolio = []

    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("Stock not found. Choose from the available stock list.")
            continue

        quantity = get_quantity(symbol)
        price = STOCK_PRICES[symbol]
        value = price * quantity

        portfolio.append(
            {
                "symbol": symbol,
                "quantity": quantity,
                "price": price,
                "value": value,
            }
        )
        print(f"Added {quantity} shares of {symbol}.")

    return portfolio


def display_portfolio(portfolio):
    if not portfolio:
        print("\nNo stocks were added.")
        return 0

    total_value = sum(item["value"] for item in portfolio)

    print("\nStock Portfolio Summary")
    print("-" * 55)
    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Value':<12}")
    print("-" * 55)

    for item in portfolio:
        print(
            f"{item['symbol']:<10}"
            f"{item['quantity']:<12}"
            f"${item['price']:<11}"
            f"${item['value']:<11}"
        )

    print("-" * 55)
    print(f"Total investment value: ${total_value}")
    return total_value


def save_as_txt(portfolio, total_value, filename="portfolio_summary.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("Stock, Quantity, Price, Value\n")
        for item in portfolio:
            file.write(
                f"{item['symbol']}, {item['quantity']}, "
                f"${item['price']}, ${item['value']}\n"
            )
        file.write(f"Total investment value: ${total_value}\n")

    print(f"Portfolio saved to {filename}")


def save_as_csv(portfolio, total_value, filename="portfolio_summary.csv"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for item in portfolio:
            file.write(
                f"{item['symbol']},{item['quantity']},"
                f"{item['price']},{item['value']}\n"
            )
        file.write(f"Total,,,{total_value}\n")

    print(f"Portfolio saved to {filename}")


def ask_to_save(portfolio, total_value):
    if not portfolio:
        return

    choice = input("\nSave result? Enter txt, csv, or no: ").strip().lower()

    if choice == "txt":
        save_as_txt(portfolio, total_value)
    elif choice == "csv":
        save_as_csv(portfolio, total_value)
    else:
        print("Result not saved.")


def main():
    print("Stock Portfolio Tracker")
    show_available_stocks()
    portfolio = build_portfolio()
    total_value = display_portfolio(portfolio)
    ask_to_save(portfolio, total_value)


if __name__ == "__main__":
    main()
