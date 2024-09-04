# Created by Ellen at 9/4/2024
Feature: Functionality of product page

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for hat
    And  Click on Add to Cart button
    And  Store product name
    And  Confirm Add to Cart button from side navigation
    And  Open cart page
    Then Verify cart has 1 item(s)
    And  Verify cart has correct product