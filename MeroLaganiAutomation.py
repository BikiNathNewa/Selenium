#importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

#installing driver
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#selecting website
url = "https://merolagani.com/Index.aspx"

driver.get(url)
driver.maximize_window()
title = driver.title
time.sleep(2)
print(title)

#clicking on live market
market = driver.find_element(By.XPATH, "//*[@id='navbar']/ul[1]/li[2]/a")
market.click()
time.sleep(2)

#dismissing alert
try:
    alert = Alert(driver)
    alert.dismiss()
except:
    print("No alert found.")
time.sleep(2)
    
live_market = driver.find_element(By.XPATH, "//*[@id='navbar']/ul[1]/li[2]/ul/li[1]/a")
live_market.click()
time.sleep(2)

#finding and clicking on company
driver.execute_script("window.scrollBy(0,400);")
time.sleep(2)

company = driver.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_LiveTrading']/table/tbody/tr[4]/td[1]/a")
company.click()
time.sleep(2)

#switching to the newly opened window
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)

driver.execute_script("window.scrollBy(0,950);")
time.sleep(2)

#clicking on price history tab
price_history = driver.find_element(By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab']")
price_history.click()
time.sleep(2)

#sorting price history by date
price_date=driver.find_element(*(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter']"))
price_date.send_keys("03/20/2025")
time.sleep(2)

search=driver.find_element(*(By.XPATH,"//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lbtnSearchPriceHistory']"))
search.click()
time.sleep(2)

#scrolling down for better view
driver.execute_script("window.scrollBy(0,100);")
time.sleep(5)

driver.quit()