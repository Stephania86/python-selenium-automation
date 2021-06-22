import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\\Users\\HP\\Downloads\\automation\\python-selenium-automation\\chromedriver.exe")
driver.get('https://www.google.com/')
search = driver.find_element(By.Name, 'q')
search.clear()
search.send_keys('watch ')
time.sleep(4)
driver.close()