from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
@when('Open cart page')
def open_cart(context):
    #context.driver.get('https://www.target.com/cart')
    context.app.cart_page.open_cart_page()

@then('Verify cart has correct product')
def verify_product_name(context):
    # actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    # print(f'Actual product in cart name: {actual_name}')
    # assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"
    context.app.cart_page.correct_product()

@then('Verify cart has {amount}(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.cart_summary(amount)
   # CART_SUMMARY = (By.CSS_SELECTOR, '[id="cart-summary-heading"]')
    #cart_summary = context.driver.find_element(*CART_SUMMARY).text
    #print(cart_summary)


@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart(context, expected_text):
    context.app.cart_page.verify_empty_cart(expected_text)


