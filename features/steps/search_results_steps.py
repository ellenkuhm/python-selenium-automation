from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # where explicit wait is used
from behave import then, when
from time import sleep

# LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
# PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
# PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    # context.driver.find_element(*ADD_TO_CART_BTN).click() #always click on the 1st Add to cart btn
    # # sleep(5)
    # context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME)) # explicit wait
    context.app.cart_page.click_add_to_cart()

@when('Store product name')
def store_product_name(context):
    context.app.cart_page.store_product_name()

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.cart_page.side_nav_add_to_cart()
    sleep(3)

@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)

@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    context.app.search_results_page.verify_product_in_url(expected_product)


@then('Verify that every product has a name and an image') # uses a loop to execute
def verify_products_name_img(context):
    context.app.search_results_page.verify_products_name_img()

# @then('Verify that every product has a name and an image') # uses a loop
# def verify_products_name_img(context):
#         # To see ALL listings (comment out if you only check top ones):
#         context.driver.execute_script("window.scrollBy(0,2000)", "") # execute_script command allows you to execute javascript object page,
#         sleep(4) # put in a sleep to give enough time for all the products and images on the page to load, not neccesarry if for only top products
#         context.driver.execute_script("window.scrollBy(0,2000)", "") # telling window to keep scrolling down the page, by (X,X) amount of pixels
#
#         all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]
#
#         for product in all_products:
#             title = product.find_element(*PRODUCT_TITLE).text # find the title that is in the product (find an element inside the element)
#             assert title, 'Product title not shown' # checking if string is not empty
#             print(title) # prints the string
#             product.find_element(*PRODUCT_IMG) # find the product's image after the title


@when ('Hover favorites icon')
def hover_element(context):
    context.app.search_results_page.hover_fav_icon()


@then ('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results_page.verify_fav_tooltip()