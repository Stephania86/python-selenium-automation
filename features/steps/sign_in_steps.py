from selenium.webdriver.common.by import By
from behave import given, when, then


@then("verify sign page oppened")
def verify_sign_page_oppened(context):
    # context.driver.find_element(By.ID, 'app_email')
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
