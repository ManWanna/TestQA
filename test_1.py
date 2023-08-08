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
# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == "Product"
# print("GOOD")
now_date = datetime.datetime.utcnow().strftime("%Y,%m,%d,%H,%M,%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\Users\\055\\PycharmProjects\\TIS_05\\screen\\' + name_screenshot)

url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print(get_url)

assert url == get_url
print("Good url")

time.sleep(10)
driver.quit()