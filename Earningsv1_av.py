import requests

alpha_vantage_key = 'Y84MMO9G796B0PNO'

url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=Y84MMO9G796B0PNO'
r = requests.get(url)
data = r.json()

annual_earnings = data['annualEarnings']
quarterly_earnings = data['quarterlyEarnings']

print([float(earning["reportedEPS"]) for earning in annual_earnings])