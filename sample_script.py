from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenuim.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\Downloads\\automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

# Implicit wait
# checks 100 ms for webelement(1/10 sec)
# only works with find_element
driver.implicitly_wait(4)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
# sleep(4)

# Explicit wait
# checks 500 ms for condition (0.5 sec)
driver.wait = WebDriverWait(driver, 4)
e = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='error, search button not clickable')

# click search
e.click()

driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
