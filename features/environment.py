from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait # for expected conditions
from webdriver_manager.chrome import ChromeDriverManager

def browser_init(context): # function to intialize the browser
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # chrome configuration
    driver_path = r'C:\Users\Ellen\python-selenium-automation\chromedriver.exe'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service) # "context" connecting to the driver

    context.driver.maximize_window()
    context.driver.implicitly_wait(4) # only waits after find element(s)
    # explicitly_wait is when you can set a condition for your wait
    # ex: trying to set a condition for the element to be clickable before clicking the element
    context.driver.wait = WebDriverWait(context.driver, 15) # for expected conditions


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.quit()
