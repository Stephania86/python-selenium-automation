from selenium.webdriver.common.by import By
from behave import given, when, then


@when("Click orders")
def click_orders(context):
    orders = context.driver.find_element(By.ID, 'nav-orders')
    orders.click()
