import yfinance as yf

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol] += shares
        else:
            self.stocks[symbol] = shares
        print(f"Added {shares} shares of {symbol}")

    def remove_stock(self, symbol, shares):
        if symbol in self.stocks:
            if self.stocks[symbol] > shares:
                self.stocks[symbol] -= shares
                print(f"Removed {shares} shares of {symbol}")
            elif self.stocks[symbol] == shares:
                del self.stocks[symbol]
                print(f"Removed {shares} shares of {symbol}")
            else:
                print(f"You don't own that many shares of {symbol}")
        else:
            print(f"You don't own any shares of {symbol}")

    def get_stock_data(self, symbol):
        stock = yf.Ticker(symbol)
        return stock.history(period='1d')['Close'][0]

    def track_performance(self):
        total_value = 0.0
        for symbol, shares in self.stocks.items():
            current_price = self.get_stock_data(symbol)
            value = current_price * shares
            total_value += value
            print(f"{symbol}: {shares} shares @ {current_price:.2f} = {value:.2f}")
        print(f"Total portfolio value: {total_value:.2f}")

def main():
    portfolio = Portfolio()

    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. Track Performance\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '3':
            portfolio.track_performance()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
