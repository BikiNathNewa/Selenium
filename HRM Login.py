#importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.by import By

#installing driver
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#selecting website
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(url)
driver.maximize_window()
title = driver.title
print(title)
time.sleep(3)

#locating and inputing username
username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")
time.sleep(3)

#locating and inputing password
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")
time.sleep(3)

#clicking login button
login = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login.click()
time.sleep(3)

#checking if login successful 
home_url = driver.current_url
if (home_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
    print("Login Successful.")
else:
    print("Login Failed.")
    
time.sleep(5)

driver.quit()