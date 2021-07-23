from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on the dog image')
def click_img(context):
    context.driver.find_element(By.CSS_SELECTOR, "ing#d").click()
    sleep(1)

@when('Switch to the new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)
    sleep(1)


@when('Return to original Window')
def switch_to_original_window(context):
    context.driver.switch_to_window(context.original_window)


@then('Verify Amazon Blog url')
def verify_blog_url(context):
    assert 'https://www.aboutamazon.com/' in context.driver.current_url, \
    f'Url https://www.aboutamazon.com/ not in {context.driver.current_Url}'
    sleep(1)


@then('Verify Amazon url')
def verify_base_url(context):
    assert 'https://www.amazon.com/' in context.driver.current_url, \
        f'Url https://www.amazon.com/ not in {context.driver.current_Url}'
    sleep(1)


@then('close new Window')
def close_window(context):
    sleep(1)
    context.driver.close()