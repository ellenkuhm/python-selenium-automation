from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# # Start Chrome browser:
# driver_path = r'C:\Users\Ellen\python-selenium-automation\chromedriver.exe'
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)

@given('Open target circle page')
def open_target(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@then('Verify there are {number} benefit cells')
def verify_benefit_cells_amount(context, number):
    cells = context.driver.find_elements(By.CLASS_NAME, "cell-item-content")
    number = int(number) # "10" => 10
    assert len(cells) == number, f'Expected {number} cells but got {len(cells)}'