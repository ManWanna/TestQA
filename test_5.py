import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('input login')


password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print('input password')
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('click login button')

time.sleep(3)

menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
print("Click Menu Button")

time.sleep(3)

link_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()
print("Click Link About")

driver.back()
print("Go Back")
time.sleep(5)
driver.forward()
print("Go Forward")

time.sleep(3)
driver.quit()