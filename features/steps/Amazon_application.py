from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open Amazon T&C page')
def open_amazon_(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('store original Window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    sleep(1)


@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_notice(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()
    sleep(1)

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)
    sleep(1)


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_page(context):
    assert 'https://www.amazon.com/gp/help/customer/display' in context.driver.current_url, \
    f'Url https://www.amazon.com/gp/help/customer/display. not in {context.driver.current_url}'
    sleep(1)


@then('User can close new window and switch back to original')
def close_window(context):
    sleep(1)
    context.driver.close()
    context.driver.switch_to_window(context.original_window)


@then('verify the each of the 5 top links open a new page')
def verify_loop_can_thru_links(context):
    expected_links = ['Amazon Best Sellers', 'Amazon Hot New Releases', 'Amazon Movers & Shakers', 'Amazon Most Wished For', 'Amazon Gift Ideas']

    for i in range(len(expected_links)):
        context.driver.find_elements(By.CSS_SELECTOR, "#zg_tabs ul li")[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, "div#zg_banner_text_wrapper").text
        assert actual_text == expected_links[i], f'Error, link is {actual_text}, but expected {expected_links[i]}'

