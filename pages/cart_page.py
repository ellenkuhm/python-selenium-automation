# Step 2 in Page Object Model:
# Create Page Objects that inherit Base Page
# and represents a real web page (or a part of it)

from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    #SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="@web/AddToCart/FulfillmentSection"] button[id*="addToCartButton"]')
    #CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    #CART_SUMMARY = (By.CSS_SELECTOR, '[id="cart-container"] div[class="h-margin-b-tight h-text-grayDark "] span')
    CART_SUMMARY = (By.CSS_SELECTOR, '[id="cart-summary-heading"]')
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_empty_cart(self, expected_text):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text(expected_text, *self.CART_EMPTY_MSG)

    def click_add_to_cart(self):
        sleep(5)
        self.click(*self.ADD_TO_CART_BTN)
        self.wait_for_element_appear(*self.SIDE_NAV_PRODUCT_NAME)  # explicit wait

    def store_product_name(self):
        self.product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME)
        print(f'Product name: {self.product_name}')

    def side_nav_add_to_cart(self):
        sleep(3)
        self.wait_and_click(*self.SIDE_NAV_ADD_TO_CART_BTN)

    def open_cart_page(self):
        self.open_url('https://www.target.com/cart')

    def cart_summary(self, amount):
        sleep(3)
        cart_summary_text = self.find_element(*self.CART_SUMMARY).text
        print(cart_summary_text)
        #assert amount in cart_summary, f'Expected {amount} not in actual {cart_summary}'


    def correct_product(self):
        actual_name = self.find_element(*self.CART_ITEM_TITLE)
        print(f'Actual product in cart name: {actual_name}')
        self.verify_partial_text(self.product_name, actual_name)
