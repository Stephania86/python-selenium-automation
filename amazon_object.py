from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazonproduct{product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp{product_id}/')

@when('Search for {search_word}')
def search_for_product(context, search_word):
    context.app.header.input_search_word(search_word):
    context.app.header.click_search()

class searchResult(Page):
    PRODUCT_RESULT = (By.XPATH, "//div[data-component-type='s-search)

    def click_first_product(self):
        self.click(*self.PRODUCT_RESULT)
    def verify_search_worked(selfself, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT

                         )
@when('click on the first product')
def click_on_the_first_product(context):
    context.app.search_results_page.click_first_product()


@then('Verify cart has{expected_count} item')
def verify_cart_count(context, expected_count):
    context.app.header.verify_cart_count(expected_count)

