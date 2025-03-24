#importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.by import By

#installing driver
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#selecting website
url = "https://www.mindrisers.com.np/online-admission"

driver.get(url)
driver.maximize_window()
title = driver.title
print(title)
time.sleep(3)

driver.execute_script("window.scrollBy(0, 900);")
time.sleep(3)

#locating and inputing names
# fullname = driver.find_element(By.ID, "full_name")
# fullname.send_keys("Biki Nath Newa")
# time.sleep(3)

# email = driver.find_element(By.NAME, "email")
# email.send_keys("bikinathnewa@gmail.com")
# time.sleep(3)

# phone_no = driver.find_element(By.ID, "mobile_no")
# phone_no.send_keys("9840724662")
# time.sleep(3)

# college = driver.find_element(By.NAME, "college")
# college.send_keys("VelTech University")
# time.sleep(3)

# qualification = driver.find_element(By.ID, "qualification")
# qualification.click()
# time.sleep(3)
# qualification_inp = driver.find_element(By.XPATH, "//*[@id='qualification']/option[2]")
# qualification_inp.click()
# time.sleep(3)

# course = driver.find_element(By.ID, "course")
# course.click()
# time.sleep(3)
# course_inp = driver.find_element(By.XPATH, "//*[@id='course']/option[5]")
# course_inp.click()
# time.sleep(3)

# schedule = driver.find_element(By.NAME, "shedule")
# schedule.click()
# time.sleep(3)


# schedule_inp = driver.find_element(By.XPATH, "//*[@id='shedule']/option[2]")
# schedule_inp.click()
# time.sleep(3)


# /html/body/div[1]/div[1]/section/form/div[1]/div[8]/div/div[2]/input
remarks = driver.find_element(By.ID,"remarks-no")
remarks.click(2)

time.sleep(3)

queries = driver.find_element(By.NAME, "question")
queries.send_keys("How long is the course and how much does it cost?")
time.sleep(5)

driver.quit()