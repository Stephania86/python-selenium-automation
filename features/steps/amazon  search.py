from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open  Amazon  page')
def open_amazon_page(context):
   # context.driver.find_element('https://www.amazon.com/')
    context.New_package_App.main_page.open_main()


@when('Input {search_word} in search field')
def search_amazon(context, search_word):
   # context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table')
    context.New_package_App.header.input_search('search_word')

@when('click on Amazon search icon')
def click_search(context):
   # context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.New_package_App.header.input_search()

@then('verify search worked for {expected_text}')
def verify_search_worked(context, expected_text):
   # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # print(f'Actual result: {actual_result}')
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f'expected {expected_result}, but got {actual_result}'
    context.New_package_App.search_results_page.verify_search_worked(expected_text)


@then('verify 40 footer links are displayed')
def verify_footer_links_amount(context):
   link_count = len(context.driver.find_elements(By.CSS_SELECTOR, ".navFooterDescItem a.nav_a"))
   assert link_count == 40, f'expected 40 links, but got {link_count}'