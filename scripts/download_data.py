"""
script that downloads historical stock data from yahoofinance and saves it in csv format to datasets folder see scrapers.py

usage:

python download_data.py
python download_data.py ABG.JO AFI.AX ...
"""

import sys
from datetime import datetime, timedelta

from scrapers import JSEScraper, JPXScraper, Scraper, NyseScraper, ASXScraper, SSXScraper, CustomScraper

if len(sys.argv) < 1:
    ticker_symbols = sys.argv[0]
    scrapers = [
        CustomScraper(sys.argv[1:])
    ]
else:
    scrapers: list[Scraper] = [
        JSEScraper(),
        JPXScraper(),
        SSXScraper(),
        ASXScraper(),
        NyseScraper()
    ]

# from yahoofinancials import YahooFinancials

# JSE – South Africa 
# ASX – Australia 
# SSX – China 
# JPX – Japan 
# NYSE - US 


# stock = yf.Ticker('ABG.JO')

# Define the start and end date for the historical data
start_date = "2021-09-15"
end_date = "2023-09-15"

for scraper in scrapers:
    stocks = scraper.get_top_100_stocks(100)
    print(stocks)
    for stock in stocks:
        start_date = datetime(2019, 9, 15)
        end_date = start_date.replace(year=start_date.year + 4)

        scraper.download_stock_data(stock, start_date=start_date, end_date=end_date, interval="1d")
        # scraper.download_stock_data(stock, start_date="2023-07-15", end_date="2023-09-15", interval="15m")
        # scraper.download_stock_data(stock, start_date="2023-09-8", end_date="2023-09-15", interval="1m")
