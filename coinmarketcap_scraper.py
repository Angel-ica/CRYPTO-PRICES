from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions
import pandas as pd
import time
import urllib.request
import os
import os.path

class WebCrawl():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def get_page(self):
        self.driver.get('https://coinmarketcap.com/')
        self.driver.implicitly_wait(10)
        
    def accept_cookies(self):
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME,'body').click()
        self.driver.find_element(by=By.XPATH, value="//div[@class='cmc-cookie-policy-banner__close']").click()
        
    def choose_currency(self):
        time.sleep(2)
        change_currency=self.driver.find_element(by=By.XPATH, value="//div[@class='sc-8580441d-1 klKJWV']//button[@class='sc-476bb07-0 sc-8580441d-7 FerZc']")
        change_currency.click()
        input_preferred_currency=self.driver.find_element(by=By.XPATH, value='//div[@class="sc-785445d2-4 kzsuLu"]//input')
        input_preferred_currency.send_keys('Pound Sterling')
        time.sleep(2)
        preferred_currrency=self.driver.find_element(by=By.XPATH, value='//div[@class="sc-8580441d-3 sc-8580441d-5 hFFJRw"]//div[@class="cmc-currency-picker--icon"]')
        ActionChains(self.driver).move_to_element(preferred_currrency).click().perform()

    def decline_survey(self):
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//div[@class="sc-b1f0826a-0 cKSWpr"]//span[2]').click()

    def decline_spot_changes(self):
        time.sleep(2)
        close_btn= self.driver.find_element(by=By.XPATH, value="//div[@class='has-style']/*[name()='svg']")
        ActionChains(self.driver).move_to_element(close_btn).click().perform()
    def decline_diamonds_and_awards(self):
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//div[@class="buttons"]//button[2]').click()

    def decline_sign_up(self):
        #time.sleep(5)
        #WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="buttons"]//button[2]')))
        self.driver.find_element(by=By.XPATH, value='//div[@class="buttons"]//button[2]').click()

    def scroll(self):
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 9):
            self.driver.execute_script("window.scrollTo(0, {});".format(i))

    def get_top_100_coins(self):
        top_100_coins=self.driver.find_elements(by=By.XPATH, value='//div[@class="sc-f7a61dda-2 efhsPu"]//table//tbody//tr')
        self.data_dict={'Rank':[],'Time':[],'Coin':[],'Price':[],'Change in last 24h':[],'Total vol(24h)':[]}
        time.sleep(20)
        for coins in top_100_coins:
            rank=coins.find_element(by=By.XPATH, value='.//td[3]//div[@class="sc-2f217aa4-3 eyyJUo"]')
            self.data_dict['Rank'].append(rank.text)
            scraped_time=time.strftime('%H:%M:%S--%D')
            self.data_dict['Time'].append(scraped_time)
            coin=coins.find_element(by=By.XPATH, value='.//td[3]//p')
            self.data_dict['Coin'].append(coin.text)
            #symbol=coins.find_element(by=By.XPATH,value= './/td//div[@class="sc-aef7b723-0 LCOyB"]//a//div//div//p')
            #self.data_dict['Symbol'].append(symbol.text)
            price=coins.find_element(by=By.XPATH, value='.//td[4]//span')
            self.data_dict['Price'].append(price.text)
            assert '£'== price.text[0]

            last_24_hours=coins.find_element(by=By.XPATH, value='.//td[6]//span')
            attr=last_24_hours.get_attribute('class')
            if 'cYiHal' in attr:
                last_24h=('▲'+str(last_24_hours.text))
                print(last_24h)
                self.data_dict['Change in last 24h'].append(last_24h)
            elif 'bQjSqS'  in attr:
                last_24h=('▼'+str(last_24_hours.text))
                print(last_24h)
                self.data_dict['Change in last 24h'].append(last_24h)

            #NOTE UNICODE CHARACTER FOR THE SIGN IS 'U+02D1'

            volume_24h_GBP=coins.find_element(by=By.XPATH, value='.//td//div[@class="sc-aef7b723-0 sc-ba1a4d26-0 QisKn"]//a//p')
            self.data_dict['Total vol(24h)'].append(volume_24h_GBP.text)
        print(self.data_dict)
        return self.data_dict
                
    def store_in_csv(self):
        df=pd.DataFrame(self.data_dict)
        assert not df.empty
        df.to_csv("coin_marketcap_data.csv",index=False,header=True)
        print('done')
        time.sleep(20)
        self.driver.quit()
        return os.path.isfile('coin_marketcap_data.csv')
        
def run():
    crawl=WebCrawl()
    crawl.get_page()
    #crawl.decline_spot_changes()
    crawl.accept_cookies()
    crawl.choose_currency()
    crawl.scroll()
    #crawl.decline_diamonds_and_awards()
    #crawl.decline_sign_up()
    #crawl.decline_survey()
    crawl.get_top_100_coins()
    crawl.store_in_csv()

if __name__=='__main__':
    run()


