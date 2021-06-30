from selenium.webdriver.common.by import By
from behave import given, when, then


@then('verify hamburger menu icon is visible')
def verify_ham_menu_is_visible(context):
    context.driver.find_element(By.label, 'Open Menu')