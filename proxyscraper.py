# Scrapy - table = response.xpath("//*[@id='proxylisttable']//tbody//tr[0]//td//text()")[0].extract()
def proxyScrap(*args):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import joblib
    from joblib import Parallel, delayed

    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options,executable_path="/home/coutinho/Downloads/chromedriver")
    browser.get("https://free-proxy-list.net/")

    ip = [browser.find_element_by_xpath(f"/html/body/section[1]/div/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[1]") for i in range(1,21)]
    ip = [ip.text for ip in ip]
    port = [browser.find_element_by_xpath(f"/html/body/section[1]/div/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[2]") for i in range(1,21)]
    port = [port.text for port in port]
    #ipp = dict(zip(ip,port))
    op = list(map(lambda x, y: x+':'+y, ip, port))
    browser.close()
    return op

if __name__ == "__main__":
    import time
    #start = time.time()
    #i=proxyScrap()
    #print(i)
    import joblib
    from joblib import Parallel, delayed
    start = time.time()
    tester = Parallel(n_jobs=2,verbose=100)(delayed(proxyScrap)(i) for i in range(1))
    print(tester)
    print(time.time() - start)
