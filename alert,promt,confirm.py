from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://the-internet.herokuapp.com/javascript_alerts")

but1 = browser.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
but1.click()

time.sleep(5)

alert = browser.switch_to.alert
alert.accept()

time.sleep(5)
browser.quit()