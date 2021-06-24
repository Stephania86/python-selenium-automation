from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open the Amazon page')
def Open_Amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('click on the cart section')
def search_amazon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()
    #text_box.send_keys("cart section", Keys.ENTER)


@then('verify cart value is 0')
def verify_cart_value_is_0(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").text
    print(f'Actual result: {actual_result}')
    expected_result = "0"
    assert expected_result == actual_result, f'expected {expected_result}, but got {actual_result}'
