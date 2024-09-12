# Step 1 in Page Object Model:
# Defining Base Page

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Page:
    def __init__(self,driver): # calling Selenium driver as an argument
        self.driver = driver
        # ^ points out the driver is inside the page
        self.wait = WebDriverWait(driver, timeout=15) # pass the driver and wait 15 seconds

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator).click()

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator).click()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator): # needs astric "*" because it gets treated like two things, by.something and value of locator
        self.driver.find_element(*locator).send_keys(text) # needs astric "*" because it gets treated like two things, by.something and value of locator

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator), # EC built differently, do not need the "*", treats locator as one whole piece
            message = f'Element by locator {locator} not clickable'
        )

    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        ).click()

    def wait_for_element_appear(self, *locator): # like to see the "Your cart is empty" text in the cart page
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by locator {locator} did not appear'
        )

    def wait_until_element_disappear(self, *locator): # example: clicking on cart item from main page to the cart page or a list of products in cart and delete an item
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by locator {locator} did not disappear'
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_partial_text, *locator): # for larger headers with a lot of text
        actual_text = self.driver.find_element(*locator).text
        assert actual_text in expected_partial_text, f'Expected {expected_partial_text} not in match actual {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f'Expected {expected_partial_url} not in {actual_url}'



    # def refresh(self):

