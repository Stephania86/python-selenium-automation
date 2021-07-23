from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon product{product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')