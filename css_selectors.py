from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = r'C:\Users\Ellen\python-selenium-automation\chromedriver.exe'

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=MWZ06PRERMF9BV4M72ZN&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# amazon logo botton
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

#  "Create account" text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# "Your name" text box
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")

# "Mobile number or Email" text box
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# "Password" text box
driver.find_element(By.CSS_SELECTOR,"#ap_password")

# "Re-enter password" text box
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# "Create your Amazon account(Continue)" button
driver.find_element(By.CSS_SELECTOR, "#continue")

# "Conditions of Use" button/link
driver.find_element(By.CSS_SELECTOR,"#legalTextRow [href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']" )

# "Privacy Notice" button/link
driver.find_element(By.CSS_SELECTOR,"#legalTextRow [href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']" )

# "Already have an account? Sign in" button/link
driver.find_element(By.CSS_SELECTOR,"a.a-link-emphasis")