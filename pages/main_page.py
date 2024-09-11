# Step 2 in Page Object Model:
# Create Page Objects that inherit Base Page
# and represents a real web page (or a part of it)

# so MainPage can inherit from the class Page, import Page from base_page in pages package
from pages.base_page import Page
class MainPage(Page):

    def open(self):
        self.open_url('https://www.target.com/')