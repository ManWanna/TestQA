import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

number1 = browser.find_element(By.XPATH, "//*[@id='num1']")
number1_value = number1.text

number2 = browser.find_element(By.XPATH, "//*[@id='num2']")
number2_value = number2.text

sum = int(number1_value) + int(number2_value)
print(sum)

select = Select(browser.find_element(By.XPATH, "//*[@id='dropdown']"))
select.select_by_value(str(sum)) # ищем элемент с текстом "Python"
print('chose')

submit_button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button")
submit_button.click()

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()