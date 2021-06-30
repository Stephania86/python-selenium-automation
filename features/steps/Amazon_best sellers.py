from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Best Sellers page')
def open_amazon_best_seller(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/')


@then('Verify that are 5 links')
def verify_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "div#zg_tabs ul li a")
    assert len(links) == 5, f'got {len(links)} '