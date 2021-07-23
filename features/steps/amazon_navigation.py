from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')



@when('click on the first product')
def click_on_the_first_product(context):
    context.driver.find_element(By.CLASS_NAME, 's-image').click()


@when('click on Add to cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('verify cart has 1 item')
def verify_cart_1_item(context):
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    print(f'Actual result: {actual_result}')
    expected_result = '1'
    assert expected_result == actual_result, f'expected {expected_result}, but got {actual_result}'

