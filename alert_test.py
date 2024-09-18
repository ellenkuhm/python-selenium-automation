from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# driver_path = ChromeDriverManager().install()
driver_path = r'C:\Users\Ellen\python-selenium-automation\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://demo.automationtesting.in/Alerts.html')

driver.find_element(By.CSS_SELECTOR, '[class="btn btn-danger"]').click()

sleep(3)

Alert(driver).accept() #to accept the alert
# Alert().dismiss() #to dismiss the alert
print('Test Passed')

driver.quit()