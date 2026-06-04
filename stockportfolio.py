import csv

def stock_portfolio_tracker():
    # Hardcoded dictionary defining current stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 420,
        "AMZN": 175,
        "GOOGL": 150
    }
    
    portfolio = []
    total_investment = 0
    
    print("--- Stock Portfolio Tracker ---")
    print("Available stocks to track: AAPL, TSLA, MSFT, AMZN, GOOGL\n")
    
    while True:
        stock_name = input("Enter stock symbol (or type 'done' to finish): ").upper().strip()
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print(f"Error: {stock_name} is not in our system. Please try a valid stock.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid whole number for quantity.")
            continue
            
        # Calculation
        price = stock_prices[stock_name]
        total_cost = quantity * price
        total_investment += total_cost
        
        # Save current entry
        portfolio.append({
            "Stock": stock_name,
            "Quantity": quantity,
            "Price per Share": price,
            "Total Value": total_cost
        })
        print(f"Added {quantity} shares of {stock_name}.\n")

    # Display Results
    if not portfolio:
        print("\nNo stocks added. Portfolio is empty.")
        return

    print("\n" + "="*40)
    print("YOUR STOCK PORTFOLIO SUMMARY")
    print("="*40)
    for item in portfolio:
        print(f"Stock: {item['Stock']} | Quantity: {item['Quantity']} | Price: ${item['Price per Share']} | Total: ${item['Total Value']}")
    print("-"*40)
    print(f"TOTAL PORTFOLIO INVESTMENT VALUE: ${total_investment}")
    print("="*40)
    
    # Optional: Save the results to a CSV file
    save_choice = input("Do you want to save your portfolio to a file? (yes/no): ").lower().strip()
    if save_choice in ['yes', 'y']:
        filename = "portfolio_summary.csv"
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Stock Symbol", "Quantity", "Price per Share ($)", "Total Value ($)"])
                for item in portfolio:
                    writer.writerow([item['Stock'], item['Quantity'], item['Price per Share'], item['Total Value']])
                writer.writerow([])
                writer.writerow(["TOTAL INVESTMENT", "", "", total_investment])
            print(f"Successfully saved portfolio data to '{filename}'!")
        except IOError:
            print("An error occurred while saving the file.")

if __name__ == "__main__":
    stock_portfolio_tracker()