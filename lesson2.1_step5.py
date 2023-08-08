from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    input1 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input1.send_keys(y)
    time.sleep(2)

    check_robot = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
    check_robot.click()
    time.sleep(2)

    radio_robot = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    radio_robot.click()
    time.sleep(2)

    submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()