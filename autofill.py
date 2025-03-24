#importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
import random
import string
from selenium.webdriver.common.by import By

#installing driver
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#selecting website
url = "https://www.mindrisers.com.np/contact-us"

def generate_email():
    domain = "abc.com"
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

def generate_name():
    random_string_1 = ''.join(random.choices(string.ascii_letters, k=8))
    random_string_2 = ''.join(random.choices(string.ascii_letters, k=8))
    name = random_string_1 + " " + random_string_2
    return name

def generate_phone():
    return "+977-98"+''.join(random.choices(string.digits, k=8))

def choose_subject():
    subjects = ["QA Testing", "DevOps", "Debugging", "Mern", "Flutter"]
    chosen = subjects[random.randrange(1,6)]
    return chosen

def generate_query():
    name = ""
    for i in range(random.randrange(3,7)):
        j = random.randrange(3, 5)
        random_string = ''.join(random.choices(string.ascii_letters, k=j))
        name = name + " " + random_string
    return  name.strip()

driver.get(url)
driver.maximize_window()
time.sleep(3)
title = driver.title
print(title)

driver.execute_script("window.scrollBy(0, 720)")
time.sleep(2)

name_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
name_field.clear()
name_field.send_keys(generate_name())
time.sleep(2)

email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
email_field.clear()
email_field.send_keys(generate_email())
time.sleep(2)

phone = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
phone.clear()
phone.send_keys(generate_phone())
time.sleep(2)

subject = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
subject.clear()
subject.send_keys(choose_subject())
time.sleep(2)

queries = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))
queries.clear()
queries.send_keys(generate_query())

time.sleep(5)

driver.quit()
