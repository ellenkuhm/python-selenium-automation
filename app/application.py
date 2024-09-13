# references to all the page objects that we implemented
# this class organizes better and reduces what is in environment
# add to environment "context.app = Application(context.driver)"
# add to environment "from app.application import Application"
from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPolicePage
from pages.tc_page import TCPage
from pages.create_account_page import CreateAccountPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicePage(driver)
        self.tc_page = TCPage(driver)
        self.create_account_page = CreateAccountPage(driver)