from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
#driver_path = ChromeDriverManager().install()
driver_path = r'C:\Users\Ellen\python-selenium-automation\chromedriver.exe'

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open url
driver.get('https://www.target.com/')

sleep(5)
# click sign in button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']//span").click()

sleep(5)
# click sign-in button from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span").click()

sleep(5)
# verify sign-in page opened
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1//span").text
# print(actual_text)
assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'