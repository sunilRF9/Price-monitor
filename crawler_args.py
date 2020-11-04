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

cluster = MongoClient('mongodb://admin:password@localhost:27017')
db = cluster['Test']
collection = db['nest']
#collection = db['pcbuild']

def getTitle(link):
    browser.get(str(link))
    title = browser.find_element_by_xpath(title_xpath)
    return title.text

def scraper(k,link):
    price_dict ={}
    product_titles = []
    try:
        browser.get(str(link))
        data = browser.find_element_by_xpath(price_xpath)
        title = browser.find_element_by_xpath(title_xpath)
        print(data.text)
        print(title.text)
        price_dict[title.text] = str(data.text).strip()
        #print(price_dict)
        product_titles.append(title.text)
        setcache(k, data.text)
        #new = {'_id': k, 'title': title.text.strip(), 'price': data.text}
        #new = {
        #        "date" : datetime.today().strftime('%Y-%m-%d'),
        #        "data" : price_dict
        #        }
        #collection.insert_one(new, check_keys=True)
        #print(new)
    except:
        browser.get(str(link))
        data = browser.find_element_by_xpath(deal_xpath)
        title = browser.find_element_by_xpath(title_xpath)
        print(data.text)
        print(title.text)
        #price_dict[title.text] = str(data.text).strip()
        price_dict[title.text] = str(data.text).strip()
        #print(price_dict)
        product_titles.append(title.text)
        setcache(k, data.text)
        #new = {'_id': k, 'title': title.text.strip(), 'price': data.text}
        #new = {
        #        "date" : datetime.today().strftime('%Y-%m-%d'),
        #        "data" : price_dict
        #        }
        #collection.insert_one(new)
        #print(new)
    #return price_dict
    return compute(price_dict)

if __name__ == "__main__":
    #import concurrent.futures
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    futs = [executor.submit(scraper, link) for link in links]
    #    #futs = executor.map(scraper, links)
    #    print(sum([fut.result() for fut in concurrent.futures.as_completed(futs)]))
    start = time.time()
    op = [scraper(k,link) for k,link in enumerate(links, start=1)]
    #temp = {'date':datetime.today().strftime('%Y-%m-%d'),
    #        'data':op}
    #collection.insert_one(temp)
    #titles = [getTitle(link) for link in links]
    #with open('f1.txt','w') as f:
    #    for title in titles:
    #        f.write('%s\n'% title)
    #both = list(map(lambda x, y: x+':'+y, op, titles))
    #print(titles)
    print(op)
    print(sum(op))
    print(round(time.time()-start,2))
    #import joblib
    #from joblib import Parallel, delayed
    #start = time.time()
    #tester = Parallel(n_jobs=-1,verbose=100, backend='threading')(delayed(scraper)(browser.get(link)) for link in links)
    #print(tester)
    #print(round(time.time()-start,2))
    browser.close()
    browser.quit()
    #from twilio.rest import Client
    #import os
    #account_sid = os.environ['TWILIO_SID']
    #account_token = os.environ['TWILIO_AUTH_TOKEN']
    #client = Client(account_sid, account_token)
    #client.messages.create(
    #        to=os.environ['MOB_NO'],
    #        from_= "+12055798923",
    #        body=str(op)
    #)
