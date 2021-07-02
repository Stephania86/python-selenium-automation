from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon Product {product_id} page')
def  open_amazon_product(context, product_id):
   context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@then('Verify user can click through colors')
def verify_loop_can_thru_colors(context):
   expected_colors = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Gray', 'Green', 'Khaki', 'Pink', 'White', 'Yellow']
   color_webelements = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

   for i in range(len(color_webelements)):
      color_webelements[i].click()
      actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
      assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected{expected_colors[i]}'
