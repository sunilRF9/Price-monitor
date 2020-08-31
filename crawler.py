from links import links
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

xp='//*[@id="priceblock_ourprice"]'

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options,executable_path="/home/coutinho/Downloads/chromedriver")

price_xpath = "//*[@id='priceblock_ourprice']"
title_xpath = '//*[@id="productTitle"]'
price_dict ={}
for k,i in enumerate(links, start=1):
    try:
        browser.get(i)
        print("opened site", i)
        data = browser.find_element_by_xpath(xp)
        title = browser.find_element_by_xpath(title_xpath)
        price_dict[title.text]=str(data.text).strip()
    except Exception as e:
        print(e)
    #print(k,title.text,"-->",data.text)
#price_dict = json.loads(price_dict)
print(price_dict)
browser.close()
