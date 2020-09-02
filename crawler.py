from utils import links, getUserAgent, getProxy, compute
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument(f'user-agent={getUserAgent()}')
#options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0')
#options.add_argument(f'--proxy-server={getProxy()}')

browser = webdriver.Chrome(options=options,executable_path="/home/coutinho/Downloads/chromedriver")

price_xpath = '//*[@id="priceblock_ourprice"]'
title_xpath = '//*[@id="productTitle"]'

price_dict ={}
for k,i in enumerate(links, start=1):
    try:
        browser.get(i)
        #print("opened site", i)
        data = browser.find_element_by_xpath(price_xpath)
        title = browser.find_element_by_xpath(title_xpath)
        price_dict[title.text] = str(data.text).strip()
    except Exception as e:
        print(e)
    #print(k,title.text,"-->",data.text)
#price_dict = json.loads(price_dict)
print(price_dict)
print("Total Cost -->",compute(price_dict))
browser.close()
