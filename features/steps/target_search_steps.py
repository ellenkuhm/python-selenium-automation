from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Search for product')
def search_product(context):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

@when('Click on cart icon')
def cart_status(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='cart 0 items']").click()

@then('Verify cart is empty')
def verify_cart_status(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    # print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

@when('Click Sign In')
def sign_in_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
sleep(2)
@when('From right side navigation, click Sign in')
def sidebar_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span").click()
    #context.driver.find.element(By.CSS_SELECTOR, "a[href='/account']")
sleep(2)

@then('Verify Sign In form opened')
def verify_sign_in_opened(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//h1//span").text
    # print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'