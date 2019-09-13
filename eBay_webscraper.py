# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd 
from selenium.common.exceptions import NoSuchElementException

# a list
result_list = []

# specify the url
urlpage = 'https://www.ebay.com/sch/Womens-Clothing/15724/i.html?_from=R40&_nkw=&_udlo=&_udhi=&_ftrt=901&_ftrv=1&_sabdlo=&_sabdhi=&_samilow=&_samihi=&_sadis=15&_stpos=97213&_dmd=1&_fosrp=1&_sop=1&_dcat=15724&Brand=Nike&LH_Complete=1&LH_Sold=1' 
print(urlpage)

# run firefox webdriver from executable path of your choice 
driver = webdriver.Firefox()

# get web page
driver.get(urlpage)


for page_num in range(0, 2):
    # execute script to scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

    # sleep for 5s
    time.sleep(5)

    results = driver.find_elements_by_class_name("vip") # 50 results per page. But useless...
    button = driver.find_elements_by_class_name('pagn-next')[0]
    button.click()
    
    print('Number of results', len(results))
    result_list.append(results)

df = pd.DataFrame(results)
df.head()
df.to_csv('eBay_scrape.csv')

'''
with open('eBay_scrape.json', 'w') as outfile:
    json.dump(results, outfile)
'''

driver.quit()



