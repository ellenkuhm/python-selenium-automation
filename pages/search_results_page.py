# Step 2 in Page Object Model:
# Create Page Objects that inherit Base Page
# and represents a real web page (or a part of it)
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # where explicit wait is used
from behave import then, when
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class SearchResultsPage(Page):
    # SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    SEARCH_RESULTS_TXT = (By.XPATH, "//span[contains(@class, 'h-text-bs')]")
    FAV_BTN = (By.CSS_SELECTOR, '[data-test="FavoritesButton"]')
    LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
    FAV_TOOLTIP_TXT = (By.XPATH, "//div[text()= 'Click to sign in and save' or starts-with(text(),'Favorited!')]")

    def verify_search_results(self, expected_product):  # the function
        # self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)
        # from the base page it is: assert actual_text in expected_partial_text
        # we need: assert expected_partial_text in actual_text, base page
        print(f'Expected product: {expected_product}')
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert expected_product in actual_text, f'Expected {expected_product} not in {actual_text}'

    def verify_product_in_url(self, expected_product): # making it dynamic with "expected_product" variable
        #self.verify_partial_url(expected_product) # from the base page
        actual_url = self.driver.current_url
        print(f'Actual url:{actual_url}')
        print(f'Expected product: {expected_product}')

    def verify_products_name_img(self):
        all_products = self.driver.find_elements(*self.LISTINGS)[:4]  # (WebEI1, WebEI2, WebEI3, WebEI4)

        for product in all_products: # loop
            sleep(3)
            title = product.find_element(*self.PRODUCT_TITLE).text  # find an element inside of element
            # find the title that is in the product
            assert title, "Product title not shown"  # checking if string is not empty
            print(title)
            product.find_element(*self.PRODUCT_IMG)  # find the product's image after the title

    def hover_fav_icon(self):
        self.hover_element(*self.FAV_BTN) # calling from the base page
        sleep(2)

    def verify_fav_tooltip(self):
        self.wait_for_element_appear(*self.FAV_TOOLTIP_TXT)
