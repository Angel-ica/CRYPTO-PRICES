import unittest
import time
import os.path 
import pandas as df
from sainsbury_scrape import WebCrawl as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class TestCryptoPrices(unittest.TestCase):
    def setUp(self):
        self.scraper = wb()
        self.scraper.get_page()
        self.scraper.accept_cookies()
        self.scraper.choose_currency()
        self.scraper.scroll()

    def test_currency(self):
        self.currency=self.scraper.get_top_100_coins()
        for all in self.currency['Price']:
            self.assertIn('£',all[0])

    def test_to_csv(self):
        # file=self.scraper.store_in_csv()
        # assert file.empty
        self.assert_(os.path.isfile('./coin_marketcap_data.csv'))
        
    def test_get_top_coins(self):
        top_coins={}
        self.assertEqual(type(top_coins),type(self.scraper.get_top_100_coins()))

    def tearDown(self):
        self.scraper.driver.quit()
        

if __name__=='__main__':
    unittest.main()

    
