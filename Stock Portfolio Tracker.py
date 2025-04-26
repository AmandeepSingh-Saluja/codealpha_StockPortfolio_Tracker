import requests
import json

API_KEY = ' 6IDHJNEFINMNGK5L'
BASE_URL = 'https://www.alphavantage.co/query'

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        symbol = symbol.upper()
        if symbol in self.stocks:
            self.stocks[symbol] += shares
        else:
            self.stocks[symbol] = shares
        print(f"Added {shares} shares of {symbol}.")

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol} from portfolio.")
        else:
            print(f"{symbol} not found in portfolio.")

    def get_stock_price(self, symbol):
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        try:
            price = float(data['Global Quote']['05. price'])
            return price
        except (KeyError, ValueError):
            print(f"Error fetching data for {symbol}.")
            return None

    def show_portfolio(self):
        if not self.stocks:
            print("Portfolio is empty.")
            return

        print("\nYour Portfolio:")
        total_value = 0
        for symbol, shares in self.stocks.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                value = price * shares
                total_value += value
                print(f"{symbol}: {shares} shares @ ${price:.2f} = ${value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    portfolio = Portfolio()

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)

        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ")
            portfolio.remove_stock(symbol)

        elif choice == '3':
            portfolio.show_portfolio()

        elif choice == '4':
            print("Exiting Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
