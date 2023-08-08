import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# user_name = driver.find_element(By.ID, 'user-name') #ID
# user_name = driver.find_element(By.NAME, 'user-name') #NAME
# user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') FULL XPath
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys('standard_user')

password = driver.find_element(By.CSS_SELECTOR, '#password') #CSS_SELECTOR
password.send_keys('secret_sauce')

button_login = driver.find_element(By.XPATH, '//input[@value="Login"]')
button_login.click()

time.sleep(10)
driver.quit()