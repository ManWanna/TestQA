import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    span1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = int(span1.text)
    y = calc(x)

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    input2 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    input2.click()

    input3 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()

    button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
