# Step 2 in Page Object Model:
# Create Page Objects that inherit Base Page
# and represents a real web page (or a part of it)

from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    def verify_text(self): # the function
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text # inside the self
        assert 'coffee' in actual_text, f'Expected coffee not in actual {actual_text}'

    def verify_url(self): # another function
        url = self.driver.current_url # inside the self
        assert 'coffee' in url, f'Expected "coffee" not in {url}'