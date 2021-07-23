from Pages.Base-page import Page
from Pages.
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART = (By.ID, 'nav_cart-count')
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp_nav_flag_us')
    SPANISH_LANG  = (By.CSS_SELECTOR, "a[href='#switch_lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')


    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def hover_flag_icon(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def select_department(self):
        select = Select(self.find_element(*DEPARTMENT_SELECT))
        select.select_by_value('search-alias=stripbooks')




    def verify_cart_count(self, expected_count):
        self.verify_text(expected_count, *self.CART)

    #def verify_spanish_lang_present(self):
