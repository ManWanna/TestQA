import math
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://psiyavush.github.io/PostList/")

enter = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/form/button')
enter.click()

time.sleep(10)

select = Select(browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/select'))
select.select_by_value("body")

time.sleep(5)
browser.quit()
