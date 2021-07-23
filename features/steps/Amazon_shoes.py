
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@when('click on Add to cart')
def click_on_Add_to_cart(context):
     if len(context.driver.find_elements(By.ID, 'native_dropdown_selected_size_name')) == 1:
        # Click on Size DD
        context.driver.find_element(By.ID, 'size_name_4')
        # Click on 2nd size option
        context.driver.find_element(By.ID, 'native_dropdown_selected_size_name').click()
        sleep(3)
        # Click on add to cart
        context.driver.find_element(By.ID, 'click_on_Add_to_cart').click()


@then('"{expected_text}" message is displayed')
def verify_empty_cart_msg(context, expected_text):
        actual_text = context.driver.find_element(By.CSS_SELECTOR, '#sc-active-cart h2').text
        assert actual_text == expected_text, f'Ex'#variation_color_name span.selection