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
    Then Verify cart has correct product


  Scenario: User can select colors
    Given Open target product A-91511634 page
    Then Verify user can click through colors