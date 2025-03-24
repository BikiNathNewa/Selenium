#importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.by import By

#installing driver
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#selecting website
url = "https://formy-project.herokuapp.com/form"

driver.get(url)
driver.maximize_window()
title = driver.title
print(title)
time.sleep(3)

#locating and inputing names
firstname = driver.find_element(By.ID, "first-name")
firstname.send_keys("Biki")
time.sleep(3)

lastname = driver.find_element(By.ID, "last-name")
lastname.send_keys("Newa")
time.sleep(3)

jobtitle = driver.find_element(By.ID, "job-title")
jobtitle.send_keys("QA Intern")
time.sleep(3)

educationlevel = driver.find_element(By.ID, "radio-button-1")
educationlevel.click()
time.sleep(3)

sex = driver.find_element(By.ID, "checkbox-1")
sex.click()
time.sleep(3)

driver.execute_script("window.scrollBy(0, 400);")

yoe = driver.find_element(By.ID, "select-menu")
#yoe.send_keys("2")
yoe.click()
yoe_select = driver.find_element(By.XPATH,"//*[@id='select-menu']/option[3]")
yoe_select.click()
time.sleep(3)

date = driver.find_element(By.ID, "datepicker")
date.send_keys("10/31/2001")
time.sleep(3)

#clicking submit button
submit = driver.find_element(By.XPATH, "/html/body/div/form/div/div[8]/a")
submit.click()
time.sleep(3)

#checking if submission successful 
home_url = driver.current_url
if (home_url == "https://formy-project.herokuapp.com/thanks"):
    print("Submission Successful.")
else:
    print("Submission Failed.")
    
time.sleep(5)

driver.quit()