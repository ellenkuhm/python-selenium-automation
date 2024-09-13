# Step 2 in Page Object Model:
# Create Page Objects that inherit Base Page
# and represents a real web page (or a part of it)

from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SearchResultsPage(Page):
    # SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    SEARCH_RESULTS_TXT = (By.XPATH, "//span[contains(@class, 'h-text-bs')]")
    def verify_search_results(self, expected_product): # the function
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT) # from the base page

    def verify_product_in_url(self, expected_product): # making it dynamic with "expected_product" variable
        #self.verify_partial_url(expected_product) # from the base page
        actual_url = self.driver.current_url
        print(f'Actual url:{actual_url}')
        print(f'Expected product: {expected_product}')
