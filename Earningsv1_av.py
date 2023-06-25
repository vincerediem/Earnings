import requests
import pandas as pd

alpha_vantage_key = 'Y84MMO9G796B0PNO'

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
        url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=' + stock + '&apikey=Y84MMO9G796B0PNO'
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
    
annual_earnings, quarterly_earnings = earnings_history(stock_list)