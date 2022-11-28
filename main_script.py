'''To ease functionality of our docker image, this script runs both scrapers.'''
from cryptocompare_scraper import run_scraper
from coinmarketcap_scraper import run



def script():
    run_scraper()
    run()

if __name__ == '__main__':
    script()

