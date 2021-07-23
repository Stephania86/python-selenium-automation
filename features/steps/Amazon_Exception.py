from behave import given, When, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
'''

@when('Click orders')
def click_orders(context):
    orders_link = context.driver.find_element(By.ID, 'nav-orders')
    print(orders_link)
    context.driver.refresh()
    orders_link = context.driver.find_element(By.ID, 'nav-orders')
    print(orders_link)
    orders_link.click()
    
'''