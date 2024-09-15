from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
    SIDE_NAV_SIGN_IN_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']//span")
    SIGN_IN_MSG = (By.XPATH, "//h1//span")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")
    ENTER_EMAIL = (By.ID, "username")
    ENTER_PASSWORD = (By.ID, "password")
    SIGN_IN_WITH_PASSWORD_BTN = (By.ID, "login")
    INCORRECT_PASSWORD_MSG = (By.XPATH, "//div[@text() = 'That password is incorrect.']")

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

    def sign_in_email(self, email):
        self.input_text(email, *self.ENTER_EMAIL)

    def sign_in_incorrect_password(self, incorrect_password):
        self.input_text(incorrect_password, *self.ENTER_PASSWORD)

    def sign_in_click_sign_in_with_password(self):
        self.click(*self.SIGN_IN_WITH_PASSWORD_BTN)

    def sign_in_incorrect_password_msg(self):
        self.find_element(*self.INCORRECT_PASSWORD_MSG)