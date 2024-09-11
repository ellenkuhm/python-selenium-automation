# Step 2 in Page Object Model:
# Create Page Objects that inherit Base Page
# and represents a real web page (or a part of it)

from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    def verify_empty_cart(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)
