from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon help page')
def Open_Amazon(context):
  context.driver.get('https://www.amazon.com/gp/help/customer/display.html ')


@when('type cancel order in the search field')
def search_amazon(context):
    text_box = context.driver.find_element(By.ID, 'helpsearch')
    text_box.send_keys("Cancel Order", Keys.ENTER)


@then('verify sign in page works')
def verify_sign_in_works(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    print(f'Actual result: {actual_result}')
    expected_result = "Cancel Items or Orders"
    assert expected_result == actual_result, f'expected {expected_result}, but got {actual_result}'

