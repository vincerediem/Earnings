from alpha_vantage.timeseries import TimeSeries

def get_earnings(stocks):
    api_key = 'YOUR_API_KEY'  # Replace with your Alpha Vantage API key
    ts = TimeSeries(key=api_key)

    earnings_data = {}

    for stock in stocks:
        try:
            data, _ = ts.get_earnings(symbol=stock)
            quarterly_earnings = []

            # Get the earnings for the last four quarters
            for i in range(4):
                earnings = data[f'quarter{i + 1}']
                quarterly_earnings.append(earnings)

            earnings_data[stock] = quarterly_earnings

        except Exception as e:
            earnings_data[stock] = str(e)

    return earnings_data

# Example usage
stock_list = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
earnings = get_earnings(stock_list)

# Display earnings data
for stock, quarterly_earnings in earnings.items():
    print(f'Earnings for {stock}:')
    for i, earnings in enumerate(quarterly_earnings):
        print(f'Quarter {i+1}: {earnings}')
    print()
