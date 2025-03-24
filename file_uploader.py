#importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.by import By

#installing driver
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#selecting website
url = "https://filebin.net"

driver.get(url)
driver.maximize_window()
title = driver.title
print(title)
time.sleep(3)

upload = driver.find_element(*(By.XPATH,"//input[@id='fileField']"))
upload.send_keys(r"C:/Users/Bravo Mike/Pictures/Camera Roll/munj.png")
time.sleep(1)

i = int(1)
home_url = driver.current_url
while i == 1:
    if (home_url == url):
        print("Not redirected yet.")
        home_url = driver.current_url
    else:
        print("Redirected successful.")
        i = 2
        time.sleep(3)

drop_down = driver.find_element(*(By.XPATH,"//a[@id='dropdownFileMenuButton']"))
drop_down.click()
time.sleep(2)

drop_down_inp = driver.find_element(*(By.XPATH,"//a[normalize-space()='Download file']"))
drop_down_inp.click()
time.sleep(2)

download = driver.find_element(*(By.XPATH,"//a[normalize-space()='Proceed to download']"))
download.click()
time.sleep(5)

driver.quit()
