from utils import links, getUserAgent, getProxy, compute
import concurrent.futures
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument(f'user-agent={getUserAgent()}')
#options.add_argument(f'--proxy-server={getProxy()}')
browser = webdriver.Chrome(options=options,executable_path="/home/coutinho/Downloads/chromedriver")

price_xpath = '//*[@id="priceblock_ourprice"]'
title_xpath = '//*[@id="productTitle"]'

def scraper():
    price_dict ={}
    start = time.time()
    for k,i in enumerate(links, start=1):
        try:
            browser.get(i)
            data = browser.find_element_by_xpath(price_xpath)
            title = browser.find_element_by_xpath(title_xpath)
            print(data.text)
            print(title.text)
            price_dict[title.text] = str(data.text).strip()
        except Exception as e:
            print(e)
    print(price_dict)
    print("Total Cost -->",compute(price_dict))
    print(round(time.time()-start,2))
if __name__ == "__main__":
    scraper()
