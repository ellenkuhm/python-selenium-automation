# Created by Ellen at 9/3/2024
Feature: Target cart status and Target log-in tests

  Scenario: User can verify that cart is empty
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty

  Scenario: User can sign-in after being logged out
    Given Open target main page
    When Click Sign In
    When From right side navigation, click Sign in
    Then Verify Sign In form opened