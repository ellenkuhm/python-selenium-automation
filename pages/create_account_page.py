from pages.base_page import Page
from selenium.webdriver.common.by import By

class CreateAccountPage (Page):
    SIDE_NAV_CREATE_ACCN_BTN = (By.ID, "listaccountNav-createAccount")
    CREATE_ACCN_MSG = (By.XPATH, "//*[text()='Create your Target account']")
    ENTER_EMAIL_CREATE_ACCOUNT = (By.NAME, "usernamecreateaccount")
    ENTER_FIRST_NAME = (By.ID, "firstname")
    KEEP_SIGNED_IN = (By.ID, "keepMeSignedIn")
    CREATE_ACCN_BTN = (By.ID, "createAccount")
    ENTER_LAST_NAME = (By.ID, "lastname")
    CREATE_PASSWORD = (By.NAME, "passwordcreateaccount")
    # JOIN_TARGET_CIRCLE = (By.)

    def click_create_account(self):
        self.click(*self.SIDE_NAV_CREATE_ACCN_BTN)

    def create_accn_msg(self,expected_text):
        self.verify_text(expected_text, *self.CREATE_ACCN_MSG)

    def create_account_email(self, email):
        self.input_text(email, *self.ENTER_EMAIL_CREATE_ACCOUNT)

    def create_account_first_name(self, first_name):
        self.input_text(first_name, *self.ENTER_FIRST_NAME)

    def create_account_last_name(self, last_name):
        self.input_text(last_name, *self.ENTER_LAST_NAME)

    def create_account_password(self, password):
        self.input_text(password, *self.CREATE_PASSWORD)

    def create_account_keep_signed_in_checkbox(self):
        self.click(*self.KEEP_SIGNED_IN)

    def create_accn_btn(self):
        self.click(*self.CREATE_ACCN_BTN)