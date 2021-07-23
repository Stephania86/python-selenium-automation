from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@when('Verify hamburger menu icon is visible')
def verify_ham_menu_visible(context):
    print('\nUSING find element\n')
    element = context.driver.find_elements(By.ID, 'nav-hamburger-menu')
    print(element)

    print('\nUSING find elementSSSS\n')
    elements = context.driver.find_elements(By.ID, 'nav-hamburger-menu')
    print(elements)