from Pages.header import Header
from Pages.Main_page import Main
from Pages.Search_results import Search_results
from product_page import ProductPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = Main(self.driver)
        self.header = Header(self.driver)
        self.product_page = ProductPage(self.driver)
        self.search_results_page = Search_results(self.driver)