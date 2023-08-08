import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[1]')
name.send_keys('Alex')

lastname = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[2]')
lastname.send_keys('Ivanov')

Email = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[3]')
Email.send_keys('k.hammet@yandex.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

input1 = browser.find_element(By.XPATH, '//*[@id="file"]')
input1.send_keys(file_path)

button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
button.click()



time.sleep(5)
browser.quit()
