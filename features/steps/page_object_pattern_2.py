from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('search for{search_word}')
def search_for_product(context, search_word):
    context.app.header.input_search_word(search_word):
    context.app.header.click_search()

@when ('click on the first product')
def click_first_product(context):
    context.app.search_results_page.click_first_product()

@then('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()

@then('verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    context.app.header.verify_cart_count(expected_count)