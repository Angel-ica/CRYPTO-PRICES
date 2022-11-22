import unittest
import time
import os.path 
from crypto_compare import WebCrawl as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class TestCryptoPrices(unittest.TestCase):
    def setUp(self):
        self.scraper = wb()
        self.scraper.get_page()
        self.scraper.scroll()
        self.scraper.choose_currency()

    def test_choose_currency(self):
        self.scraper.get_top_coins()
        assert '£' in self.scraper.data_dict['Price']


if __name__=='__main__':
    unittest.main()

    