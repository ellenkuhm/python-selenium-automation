# Step 1 in Page Object Model:
# Defining Base Page

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Page:
    def __init__(self,driver): # calling Selenium driver as an argument
        self.driver = driver
        # ^ points out the driver is inside the page
        self.wait = WebDriverWait(driver, timeout=15)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator).click()

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator).click()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)


    # def refresh(self):
    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by locator {locator} did not appear'
        )
