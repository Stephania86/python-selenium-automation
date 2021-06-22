from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\HP\Downloads\\automation\\python-selenium-automation\\chromedriver.exe")

driver.maximize_window()
driver.get('https://www.amazon.com/gp/help/customer/display.html')
search_bar = driver.find_element(By.ID, 'helpsearch')

search_bar.clear()
search_bar.send_keys('Cancel order')
sleep(3)
search_bar.send_keys(Keys.ENTER)

cancel_items = driver.find_element(By.XPATH, '//a[contains(text(), "Cancel Items or Orders")]')
assert 'Cancel Items or Orders' in cancel_items.text, 'Could no find Cancel Items or Orders text'

sleep(3)
driver.close()