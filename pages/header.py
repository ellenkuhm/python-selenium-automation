# Step 2 in Page Object Model:
# Create Page Objects that inherit Base Page
# and represents a real web page (or a part of it)

from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    def search(self):
        self.input_text('coffee', *self.SEARCH_FIELD) # locator is inside the self/argument
        self.click(*self.SEARCH_BTN) # locator is inside the self/argument
        # wait for the page with search results to load
        sleep(6)

    def click_cart(self):
            self.click(*self.CART_BTN)
            sleep(2)