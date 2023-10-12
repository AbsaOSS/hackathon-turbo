from datetime import datetime, timedelta

from scrapers import JSEScraper, JPXScraper, Scraper, NyseScraper, ASXScraper, SSXScraper

# from yahoofinancials import YahooFinancials

# JSE – South Africa 
# ASX – Australia 
# SSX – China 
# JPX – Japan 
# NYSE - US 

scrapers: list[Scraper] = [
    JSEScraper(),
    JPXScraper(),
    SSXScraper(),
    ASXScraper(),
    NyseScraper()
]

# stock = yf.Ticker('ABG.JO')

# Define the start and end date for the historical data
start_date = "2021-09-15"
end_date = "2023-09-15"

for scraper in scrapers:
    stocks = scraper.get_top_100_stocks(100)
    print(stocks)
    for stock in stocks:
        start_date = datetime(2021, 9, 15)
        end_date = start_date.replace(year=start_date.year + 2)

        scraper.download_stock_data(stock, start_date=start_date, end_date=end_date, interval="1d")
        # scraper.download_stock_data(stock, start_date="2023-07-15", end_date="2023-09-15", interval="15m")
        # scraper.download_stock_data(stock, start_date="2023-09-8", end_date="2023-09-15", interval="1m")
