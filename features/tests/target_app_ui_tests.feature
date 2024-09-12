# Created by Ellen at 9/12/2024
Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    When Store original window
    And Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When Click Sign In
    When From right side navigation, click Sign in
    When Store original window
    And Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page opened
    And Close current page
    And Return to original window
#  And User can close new window and switch back to original
