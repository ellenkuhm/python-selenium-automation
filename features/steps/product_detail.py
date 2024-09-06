from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(10)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['grey', 'black/gum', 'dark khaki', 'navy/tan', 'stone/grey', 'white/gum', 'white/navy/red', 'white/sand/tan']

    actual_colors = []
    sleep(5)

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors[12:]: # starts looping on index 12, the first shoe color
        color.click()

        selected_color = context.driver.find_elements(*SELECTED_COLOR) # find the locator of the selected color
        selected_color = selected_color[2].text # 'Color\nBlack' # get the index of the element for the color selection category
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'