from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.app.main_page.open()

@when('Search for {product}')
def search_product(context, product):
    print('Step layer:', product)
    context.app.header.search_product(product)

@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")

@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number)  # convert str "6" ==> to int 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'
    # Make sure to always assert len() for multiple elements as shown above
    # because .find_elements() function never fails.
    # This code with incorrect locator will always pass:
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav2613542']")
    print("Found elements: ")
    print(links)

    for i in range (len(links)): # number of iterations/ amount of links
        links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
        links[i].click() # take element of index 0 and click on it and then search again until go thru all the locators

        # 'statleElementReference' means you need to change the logic to only find the element right before you do the actions