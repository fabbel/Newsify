from feedly_client import FeedlyClient
from preprocess import preprocess_text
from generate_topics import generate_topics
import yfinance as yf
import json
import datetime

# Feedly API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost"
CODE = "your_code"

# Ticker data
with open('sectors.json') as f:
    sectors_data = json.load(f)

def get_ticker_data():
    # Get tickers for each sector
    sectors = list(sectors_data.keys())
    tickers = []
    for sector in sectors:
        tickers += sectors_data[sector]

    # Download ticker data
    today = datetime.date.today().strftime("%Y-%m-%d")
    ticker_data = yf.download(tickers, start="2020-01-01", end
