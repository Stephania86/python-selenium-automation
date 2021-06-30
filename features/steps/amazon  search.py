from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Input Table in search field')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table')


@when('click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('verify search worked')
def verify_search_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    print(f'Actual result: {actual_result}')
    expected_result = '"Table"'
    assert expected_result == actual_result, f'expected {expected_result}, but got {actual_result}'
