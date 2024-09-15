from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sign In')
def sign_in_click(context):
    context.app.sign_in_page.click_sign_in()
    sleep(2)
@when('From right side navigation, click Sign in')
def sidebar_sign_in(context):
    context.app.sign_in_page.side_nav_sign_in_btn()
    sleep(2)

@then('Verify Sign In form opened')
def verify_sign_in_opened(context):
    expected_text = 'Sign into your Target account'
    context.app.sign_in_page.sign_in_msg(expected_text)

@given ('Open sign In page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when ('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()

@then ('Verify Terms and Conditions page opened')
def verify_tc_opened(context):
    context.app.tc_page.verify_tc_url()

@then ('Input email for sign-in: {email}')
def input_email(context, email):
    context.app.sign_in_page.sign_in_email(email)

@then('Input incorrect password for sign-in: {incorrect_password}')
def input_incorrect_password(context, incorrect_password):
    context.app.sign_in_page.sign_in_incorrect_password(incorrect_password)

@then('Click Sign in with password button')
def click_sign_in_with_password(context):
    context.app.sign_in_page.sign_in_click_sign_in_with_password()

@then('Verify "That password is incorrect." message appears')
def incorrect_password_msg(context):
    context.app.sign_in_page.sign_in_incorrect_password_msg()
