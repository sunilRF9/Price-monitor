from flask import Flask, jsonify
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
deal_xpath = '//*[@id="priceblock_dealprice"]'
app = Flask(__name__)
@app.route('/')
def home():
    price_dict ={}
    total_price ={}
    start = time.time()
    for k,i in enumerate(links, start=1):
        try:
            browser.get(i)
            #print("opened site", i)
            data = browser.find_element_by_xpath(price_xpath)
            title = browser.find_element_by_xpath(title_xpath)
            print(data.text)
            print(title.text)
            price_dict[title.text] = str(data.text).strip()
            total = compute(price_dict)
            total_price["Total"] = total
            print("Total Cost -->",compute(price_dict))
            print(round(time.time()-start,2))
            return jsonify(price_dict,total_price)

        except:
            browser.get(i)
            #print("opened site", i)
            data = browser.find_element_by_xpath(deal_xpath)
            title = browser.find_element_by_xpath(title_xpath)
            print(data.text)
            print(title.text)
            price_dict[title.text] = str(data.text).strip()
        #print(k,title.text,"-->",data.text)
    #price_dict = json.loads(price_dict)
    #print(price_dict)
            total = compute(price_dict)
            total_price["Total"] = total
            print("Total Cost -->",compute(price_dict))
            print(round(time.time()-start,2))
            return jsonify(price_dict,total_price)

if __name__ == "__main__":
    app.run(debug=True)
