# where we put the reusable methods that all the other page objects will inherit
# a base page that stores all the generic functions, example of inheritance
class Page: # the base page with class methods

    def click(self):
        print('Clicking...')

    def verify_text(self):
        print('Verifying...')

    def input_text(self, text):
        print(f'Inputting text, {text}')


class LoginPage(Page): # page object that inherits base page (the class Page)
    def login(self): # defining login in the LoginPage class
        self.input_text('email') # "input_text" is defined in the base page, the class Page
        self.input_text('password') # "input_text" is defined in the base page, the class Page
        self.click() # "click" is defined in the base page, the class Page

class SignUpPage(Page): # page object that inherits base page
    pass

login_page = LoginPage() # variable referring to the LoginPage class
login_page.click() # uses the click function that LoginPage inherits from the base class
login_page.login() # uses the login function defined in LoginPage

# examples of page objects:
# header page object
# footer page object
# main page object
# will need to break webpages with lots of code into multiple page objects
# example:
# Main Page will break into Main Page Top Components, Main page Target Style Blog, Main Page Target Circle Deals
# header will be its own page object with side menu page object
