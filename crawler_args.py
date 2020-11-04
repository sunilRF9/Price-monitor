from utils import links, getUserAgent, getProxy, compute
from pprint import pprint
from datetime import datetime
from pymongo import MongoClient
from cache_redis import setcache, getCache
import concurrent.futures
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
#options.add_argument(f'user-agent={getUserAgent()}')
#options.add_argument(f'--proxy-server={getProxy()}')
browser = webdriver.Chrome(options=options,executable_path="/home/coutinho/Downloads/chromedriver")
price_xpath = '//*[@id="priceblock_ourprice"]'
title_xpath = '//*[@id="productTitle"]'
deal_xpath = '//*[@id="priceblock_dealprice"]'

def scraper(k,link):
    price_dict ={}
    product_titles = []
    try:
        browser.get(str(link))
        data = browser.find_element_by_xpath(price_xpath)
        title = browser.find_element_by_xpath(title_xpath)
        price_dict[title.text] = str(data.text).strip()
        product_titles.append(title.text)
        setcache(k, data.text)
    except:
        browser.get(str(link))
        data = browser.find_element_by_xpath(deal_xpath)
        title = browser.find_element_by_xpath(title_xpath)
        price_dict[title.text] = str(data.text).strip()
        product_titles.append(title.text)
        setcache(k, data.text)
    return compute(price_dict)

if __name__ == "__main__":
    start = time.time()
    op = [scraper(k,link) for k,link in enumerate(links, start=1)]
    titles = [getTitle(link) for link in links]
    print(op)
    print(sum(op))
    print(round(time.time()-start,2))
    browser.close()
    browser.quit()
