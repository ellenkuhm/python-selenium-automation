from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sign In')
def sign_in_click(context):
    context.app.sign_in_page.click_sign_in()
    sleep(2)
@when('From right side navigation, click Sign in')
def sidebar_sign_in(context):
    context.app.sign_in_page.right_side_nav_sign_in_btn()
    sleep(2)

@then('Verify Sign In form opened')
def verify_sign_in_opened(context):
    expected_text = 'Sign into your Target account'
    context.app.sign_in_page.sign_in_msg(expected_text)