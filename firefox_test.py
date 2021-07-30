import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(executable_path="./geckodriver.exe")
driver.get('https://www.google.com/')
driver.implicitly_wait(8)
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('watch ')

driver.close()