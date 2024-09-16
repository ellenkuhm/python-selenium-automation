import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application
from support.logger import logger

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

def browser_init(context, scenario_name): # function to intialize the browser
    """
    :param context: Behave context
    """

    # if 'browser' in os.environ:
    #     if os.environ['browser']== 'chrome':
    #         driver_path = ChromeDriverManager().install()
    #         service = Service(driver_path)
    #         context.driver = webdriver.Chrome(service=service)
    #
    #     elif os.environ['browser']== 'ff':
    #         driver_path = GeckoDriverManager().install()
    #         service = Service(driver_path)
    #         context.driver = webdriver.Firefox(service=service)

    # driver_path = ChromeDriverManager().install()
    # chrome configuration
    driver_path = r'C:\Users\Ellen\python-selenium-automation\chromedriver.exe'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service) # "context" connecting to the driver

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # context.driver = webdriver.Safari()

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='C:\Users\Ellen\python-selenium-automation\geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'ellenkuhm_dngxI0'
    # bs_key = 'hUnkZpTPbkg2CT4PUYXx'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #
    # options = Options()
    # bstack_options = {
    #     "os" : "OS X", # OS X,
    #     "osVersion" : "sonoma",
    #     'browserName': 'Safari',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)




    context.driver.maximize_window()
    context.driver.implicitly_wait(4) # only waits after find element(s)
    # explicitly_wait is when you can set a condition for your wait
    # ex: trying to set a condition for the element to be clickable before clicking the element
    context.driver.wait = WebDriverWait(context.driver, 15) # for expected conditions
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)

def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.quit()
