from pages.base_page import Page
from selenium.webdriver.common.by import By

class CreateAccountPage (Page):
    SIDE_NAV_CREATE_ACCN_BTN = (By.ID, "listaccountNav-createAccount")
    CREATE_ACCN_MSG = (By.XPATH, "//*[text()='Create your Target account']")
    ENTER_EMAIL = (By.ID, "username")
    ENTER_FIRST_NAME = (By.ID, "firstname")
    KEEP_SIGNED_IN = (By.ID, "keepMeSignedIn")
    CREATE_ACCN_BTN = (By.ID, "createAccount")
    ENTER_LAST_NAME = (By.ID, "lastname")
    ENTER_PASSWORD = (By.ID, "password")
    # JOIN_TARGET_CIRCLE = (By.)

    def click_create_account(self):
        self.click(*self.SIDE_NAV_CREATE_ACCN_BTN)

    def create_accn_msg(self,expected_text):
        self.verify_text(expected_text, *self.CREATE_ACCN_MSG)

    def input_email(self, email):
        self.input_text(email, *self.ENTER_EMAIL)

    def input_first_name(self, first_name):
        self.input_text(first_name, *self.ENTER_FIRST_NAME)

    def input_last_name(self, last_name):
        self.input_text(last_name, *self.ENTER_LAST_NAME)

    def input_password(self, password):
        self.input_text(password, *self.ENTER_PASSWORD)

    def keep_signed_in_checkbox(self):
        self.click(*self.KEEP_SIGNED_IN)

    def create_accn_btn(self):
        self.click(*self.CREATE_ACCN_BTN)