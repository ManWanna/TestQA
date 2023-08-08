import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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

# driver.execute_script('window.scrollTo(0, 500)')
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[3]/a")
action.move_to_element(red_t_shirt).perform()

time.sleep(3)

now_date = datetime.datetime.utcnow().strftime("%Y,%m,%d,%H,%M,%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\Users\\055\\PycharmProjects\\TIS_05\\screen' + name_screenshot)



time.sleep(4)
driver.quit()