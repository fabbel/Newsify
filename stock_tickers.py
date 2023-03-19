import yfinance as yf
import pandas as pd
import re

def get_stock_tickers(topics):
    """
    Gets relevant stock tickers for the given topics
    """
    # Define list of market sectors and their relevant stock tickers
    sectors = {
        'Technology': ['AAPL', 'MSFT', 'GOOGL', 'FB', 'TSLA'],
        'Healthcare': ['JNJ', 'PFE', 'MRNA', 'AZN', 'ABT'],
        'Finance': ['JPM', 'GS', 'BAC', 'WFC', 'C'],
        'Energy': ['XOM', 'CVX', 'BP', 'RDS-A', 'TOT'],
        'Consumer Goods': ['PG', 'KO', 'NSRGF', 'PEP', 'L
