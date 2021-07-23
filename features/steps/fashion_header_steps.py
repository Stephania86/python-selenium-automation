from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionsChains
from selenium.webdriver.common.by import By

class FashionHeader(Page):
    NEW_ARRIVALS = (By.CSS_SELECTOR, "nav-subnav a.nav-hasArrow[href*='/s/ref=']")
    WOMEN_FASHION = (By.CSS_SELECTOR, "a.mm-merch-panel[href*='/S?1=fashion-womens'] li")

   def hover_new_arrivals(self):
   new-arrivals = self.find_element(*self.NEW_ARRIVALS)
   actions = ActionsChains(self.driver)
   actions.move_to_element(new_arrivals)
   actions.perform()

   def verify_women_fashion_panel_present(self):
       self.wait_for_element_appear(*self.WOMEN-FASHION)