import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.XPATH, "//img[@id='treasure']")
x = x_element.get_attribute('valuex')
x = int(x)
y = calc(x)

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)
time.sleep(2)

input2 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
input2.click()
time.sleep(2)

input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
input3.click()
time.sleep(2)

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()