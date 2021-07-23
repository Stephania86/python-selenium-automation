from behave import given, then
from selenium.webdriver.common.by import By


@given('Open Amazon Best Sellers page')
def open_amazon_best_sellers(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/')
'''
@then('Verify that are 5 links')
def verify_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "div#zg_tabs ul li a")
    assert len(links) == 5, f'got {len(links)} '
'''

@then('Verify that are {expected_links} links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    assert len(actual_links) == int(expected_links), f' Expected{expected_links} limk'
@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(TOP_LINKS) [x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text}'

'''
TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')
 HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')
 '''