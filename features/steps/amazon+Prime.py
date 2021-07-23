from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon Prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify {box_count} benefit boxes are displayed')
def verify_benefit_boxes(context, box_count):
    box_count = int(box_count)
    boxes = context.driver.find_elements(By.CSS_SELECTOR, 'div.benefit-box')
    assert len(boxes) == box_count, f'expected {box_count} boxes, but got {len(boxes)}'