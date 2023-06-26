import requests
import pandas as pd

ALPHA_VANTAGE_KEY = 'Y84MMO9G796B0PNO'

def stock_list():
    input_str = input("Enter stocks separated by space: ")
    # Split the string and convert each value to integer, creating an array
    stock_list = input_str.split()
    return stock_list
stock_list = stock_list()

def annual_metrics(annual_earnings, stock):
    print(stock.upper() + " __annual earnings__")
    for i in annual_earnings[:5]:
        print(f"${float(i['reportedEPS'])} on {i['fiscalDateEnding']}")

def quarterly_metrics(quarterly_earnings, stock):
    print(stock.upper() + " __quarterly earnings__")
    #create dataframe to display quarterly data
    df = pd.DataFrame(quarterly_earnings[:20])
    print(df)

def earnings_history(stock_list):
    for stock in stock_list:
        url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=' + stock + '&apikey=' + ALPHA_VANTAGE_KEY
        r = requests.get(url)
        data = r.json()

        annual_earnings = data['annualEarnings']
        #contains 'reportedEPS' and 'fiscalDateEnding'

        quarterly_earnings = data['quarterlyEarnings']
        #contains fiscalDateEnding, reportedDate, reportedEPS, 
        #estimatedEPS, surprise, surprisePercentage

        annual_metrics(annual_earnings, stock)

        quarterly_metrics(quarterly_earnings, stock)


    return annual_earnings, quarterly_earnings

def price_history(stock_list):
    for stock in stock_list:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock + '&apikey=' + ALPHA_VANTAGE_KEY
        r = requests.get(url)
        data = r.json()

        closing_prices = []
        time_series = data['Time Series (Daily)']
        for date in time_series:
            closing_price = float(time_series[date]['4. close'])
            closing_prices.append(closing_price)
        
        df = pd.DataFrame({'Closing Price': closing_prices})
    
    return df

    
annual_earnings, quarterly_earnings = earnings_history(stock_list)

df = price_history(stock_list)
print(df)