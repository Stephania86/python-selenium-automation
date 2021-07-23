from selenium.webdriver.common.by import By
from behave import given, when, then
from page.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SIZE_TOOLTIP = (By.id, 'a-popover-content-1')
    SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
    SIZE_OPTION_0 = (By.ID, 'size_name_0')
    PRICE_BUY_BOX = (By.ID, 'priceInsideBuyBox-feature_div')
    COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .select')


    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)




'''
@then('verify hamburger menu icon is visible')
def verify_ham_menu_is_visible(context):
    context.driver.find_element(By.ID, 'Open Menu')
'''