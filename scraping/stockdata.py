import requests
from dotenv import load_dotenv
import os
load_dotenv() 
api_key = os.environ["ALPHA_API"]
stocks = [
    "SPY", #SPDR S&P 500 ETF Trust
    "DIA", #SPDR Dow Jones Industrial Average ETF
    "QQQ", #Invesco QQQ top 100 Nasdaq
    "IWM", #Russell 2000
    "VT", #Vanguard world stocks
    "TLT", #20+ year treasuy bond
    "IEF" #7-10 year treasury bond ETF
] #this goes in symbol field, not function

commodities = [
    "WTI", #WTI Crude Oil
    "BRENT", #Brent Crude Oil (European)
    "NATURAL_GAS", #Natural Gas
    "COPPER",
    "ALUMNIUM",
    "WHEAT",
    "CORN",
    "SUGAR", 
    "COFFEE",
    "ALL_COMMODITTIES"
] #edit function for this, not symbol

def save_daily_data(symbol):
    response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full&datatype=csv")
    if response.status_code == 200:
        data = response.text # or response.text or response.content
        f = open(f"../data/{symbol}.csv", "w")
        f.write(data)
        f.close()

def save_all():
    for i in stocks:
        save_daily_data(i)
save_all()
