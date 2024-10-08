# Created by Ellen at 9/4/2024
Feature: Target main page search tests

  @smoke @safari_only
  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee
    Then Verify correct search results URL opens for coffee

  Scenario: User can search for a mug
    Given Open target main page
    When Search for mug
    Then Verify search results shown for mug
    Then Verify correct search results URL opens for mug

  Scenario: User can search for an iphone
    Given Open target main page
    When Search for iphone
    Then Verify search results shown for iphone
    And Verify correct search results URL opens for iphone

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <expected_result>
    And Verify correct search results URL opens for <expected_result>
    Examples:
    |product  |expected_result    |
    |coffee   |coffee             |
    |tea      |tea                |
    |iphone   |iphone             |

  Scenario: Verify that user can see products
     Given Open target main page
     When Search for fruit snacks
     Then Verify that every product has a name and an image

  # example scenario of using selenium action chains (hover)
  Scenario: User can see favorites tooltip for search results
    Given Open target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown

    # * REMINDER * :
    # And will always copy the step before it for the steps