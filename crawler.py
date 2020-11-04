from utils import links, getUserAgent, getProxy, compute
import concurrent.futures
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

def scraper():
    price_dict ={}
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
        except Exception as e:
            print(e)
        #print(k,title.text,"-->",data.text)
    #price_dict = json.loads(price_dict)
    print(price_dict)
    print("Total Cost -->",compute(price_dict))
    print(round(time.time()-start,2))
if __name__ == "__main__":
    scraper()
    #with concurrent.futures.ThreadPoolExecutor(max_workers = 8) as executor:
    #    executor.submit(scraper,)
#    with concurrent.futures.ThreadPoolExecutor() as executor:
#        res = executor.map(scraper,) 
#        print(res)
#    import joblib
#    from joblib import Parallel, delayed
#    start = time.time()
#    tester = Parallel(n_jobs=2,verbose=100)(delayed(scraper)(i) for i in range(1))
#    print(tester)
