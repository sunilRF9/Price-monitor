from utils import links
import requests
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Test(unittest.TestCase):

    def test_setup_check_links(self):
        options = Options()
        price_xpath = '//*[@id="priceblock_ourprice"]'
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options,executable_path="/home/coutinho/Downloads/chromedriver")
        for k,link in enumerate(links):
            req = requests.get(link)
            if req.status_code != requests.codes['ok']:
                assert True
            print(k,link)
            if browser.get(link):
                if browser.find_element_by_xpath(price_xpath):
                    print('Product in stock')
                else:
                    print('Product out of stock')
    def teardown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
