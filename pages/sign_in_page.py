from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
    SIDE_NAV_SIGN_IN_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']//span")
    SIGN_IN_MSG = (By.XPATH, "//h1//span")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)

    def side_nav_sign_in_btn(self):
        self.click(*self.SIDE_NAV_SIGN_IN_BTN)

    def sign_in_msg(self, expected_text):
        self.verify_text(expected_text, *self.SIGN_IN_MSG)

    def open_sign_in_page(self):
        self.open_url('')

    def click_tc_link(self):
        self.click(*self.TC_LINK)

