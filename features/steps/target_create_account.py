from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('From right side navigation, click Create account')
def sidebar_create_accn(context):
    context.app.create_account_page.click_create_account()
    sleep(2)

@then('Verify Create account form opened')
def verify_create_accn_opened(context):
    expected_text = 'Create your Target account'
    context.app.create_account_page.create_accn_msg(expected_text)

@then('Input email {email}')
def input_email(context, email):
    context.app.create_account_page.input_email(email)

@then('Input First Name {first_name}') #always needs to be the same as what's in the function
def input_first_name(context, first_name):
    context.app.create_account_page.input_first_name(first_name)

@then('Input Last Name {last_name}')
def input_last_name(context, last_name):
    context.app.create_account_page.input_last_name(last_name)

@then('Input password {password}')
def input_password(context,password):
    context.app.create_account_page.input_password(password)

@then('Click Keep me signed in checkbox')
def check_keep_signed_in(context):
    context.app.create_account_page.keep_signed_in_checkbox()

@then('Click Create account button')
def click_create_accn(context):
    context.app.create_account_page.create_accn_btn()

# @then('Verify Join Target Circle page Opens')
# def verify_join_target_circle_opens(context):
#     expected_text =




