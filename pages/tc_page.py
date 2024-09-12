from selenium.webdriver.common.by import By
from pages.base_page import Page
class TCPage(Page):
    def verify_tc_url(self):
        self.verify_partial_url('/terms-conditions')