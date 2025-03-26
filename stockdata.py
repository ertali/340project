import requests
from dotenv import load_dotenv
import os
load_dotenv() 
api_key = os.environ["ALPHA_API"]
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey=NPQAG01528WX71F8&outputsize=full")
if response.status_code == 200:
    data = response.json() # or response.text or response.content
    print(data)