import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), '$100')
)

button = browser.find_element(By.XPATH, "//*[@id='book']")
button.click()

span1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(span1.text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

button1 = browser.find_element(By.XPATH, '//*[@id="solve"]')
button1.click()

time.sleep(5)
