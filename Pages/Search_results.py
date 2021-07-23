from Pages.Base_page import Page
from selenium.webdriver.common.by import By


class Search_results(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@id='nav-cart-count']")

def verify_search_worked(self, expected_text):
    # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    self.verify_text(expected_text, *self.SEARCH_RESULT)


def verify_sign_in_page_open(self):
    # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
    # expected_result = '"open"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    context.New_package_App.search_results.page.verify_sign_in_page_open()


def verify_your_shopping_cart_is_empty.(self):
    self.verify_your_shopping_cart_value(expected_text= *self.SEARCH_RESULT)
    # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
    # expected_result = '"open"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    context.New_package_App.search_results.page.verify_sign_in_page_open()

def open_the_amazon_page(self, expected_text):
    # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    self.verify_text(expected_text, *self.SEARCH_RESULT)


def search_for_coffee_mug(self, expected_text):
    # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    self.verify_text(expected_text, *self.SEARCH_RESULT)


def click_on_add_to_cart(self, expected_text):
    # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    self.verify_text(expected_text, *self.SEARCH_RESULT)

def verify_cart_has(self, expected_text):
    # actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    self.verify_text(expected_text, *self.SEARCH_RESULT)

