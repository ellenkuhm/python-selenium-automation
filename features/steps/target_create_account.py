from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('From right side navigation, click Create account')
def sidebar_create_accn(context):
    context.app.create_account_page.click_create_account()
    sleep(2)

@then('Verify Create account page form opened')
def verify_create_accn_opened(context):
    expected_text = 'Create your Target account'
    context.app.create_account_page.create_accn_msg(expected_text)

@then('Input email on create account page: {email}')
def email_create_account(context, email):
    context.app.create_account_page.create_account_email(email)

@then('Input first name on create account page: {first_name}') #always needs to be the same as what's in the function
def first_name_create_account(context, first_name):
    context.app.create_account_page.create_account_first_name(first_name)

@then('Input last name on create account page: {last_name}')
def last_name_create_account(context, last_name):
    context.app.create_account_page.create_account_last_name(last_name)

@then('Input password on create account page: {password}')
def create_account_password(context,password):
    context.app.create_account_page.create_account_password(password)

@then('Click "Keep me signed in checkbox" on create account page')
def create_account_check_keep_signed_in(context):
    context.app.create_account_page.create_account_keep_signed_in_checkbox()

@then('Click Create account button')
def click_create_accn(context):
    context.app.create_account_page.create_accn_btn()

# @then('Verify Join Target Circle page Opens')
# def verify_join_target_circle_opens(context):
#     expected_text =




