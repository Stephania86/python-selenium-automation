from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open Amazon page')
def open_amazon_(context, product_id):
   context.driver.get(f'https://www.amazon.com/{product_id}')

@when('Click orders')
def click_orders(context):
   context.driver.find_element(By.ID, 'nav-orders').click()


@when('Click Amazon Orders link')
def click_amazon_orders(context):
   # context.driver.find_element(By.ID, 'nav-orders').click()
   context.New_package_App.header.input_search()


@when('Click on cart icon')
def click_on_cart(context):
    # context.driver.find_element(By.ID, 'add-to-cart-button').click()
    context.New_package_App.header.input_search()

@then('Verify Sign In page is opened')
def verify_sign_page(context):
   context.driver.find_element(By.ID, 'ap_email').click()


@when('Click Sign In from popup')
def click_sign_in_btn(context):
   e = context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))
   e.click


@then('Verify user can click through colors')
def verify_loop_can_thru_colors(context):
   expected_colors = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Gray', 'Green', 'Khaki', 'Pink', 'White', 'Yellow']
   color_webelements = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")
   for [i] in range(len(color_webelements)):
       color_webelements[i].click()
       actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
       assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected{expected_colors[i]}'


@then('Verify Sign in popup is clickable')
def verify_sign_in_popup(context):
   context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))


@when('wait for {sec_count}sec')
def sleep_sec(context, sec_count):
   sleep(int(sec_count))


@then('verify sign in popup disappears')
def verify_signin_popup_disappears(context):
   # context.driver.wait.until(condition == True)
   # context.driver.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))
   # context.driver.wait.until_not(condition == False)
   context.driver.wait.until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))


@then('Verify Your Shopping Cart is empty')
def verify_your_shopping_cart(context):
   context.driver.find_element(By.ID, 'sc-empty-cart-message')


