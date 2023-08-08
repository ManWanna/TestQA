import math
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("https://fakturaural.com/")

# price = WebDriverWait(browser, 12).until(
#     EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), '$100')
# )

search = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/input')

search.send_keys("groove")

search.send_keys(Keys.ENTER)

time.sleep(5)

faktura = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[1]/span')

faktura = faktura.text



assert 'Фактура Урал' == faktura
print("GOOD")

time.sleep(5)



time.sleep(5)
browser.quit()
