# Scrapy - table = response.xpath("//*[@id='proxylisttable']//tbody//tr[0]//td//text()")[0].extract()
def proxyScrap():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

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
    return op[0]

if __name__ == "__main__":
    i = proxyScrap()
    print(i)
