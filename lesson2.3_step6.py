import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

span1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(span1.text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()

time.sleep(5)
browser.quit()
