# Created by Ellen at 9/4/2024
Feature: Log-in Functionality

  Scenario: User can sign-in after being logged out
    Given Open target main page
    When Click Sign In
    When From right side navigation, click Sign in
    Then Verify Sign In form opened

  Scenario: User can create account
    Given Open target main page
    When Click Sign In
    When From right side navigation, click Create account
    Then Verify Create account form opened
    Then Input email test@gmail.com
    And Input First Name test
    Then Input Last Name test
    Then Input password test
    And Click Keep me signed in checkbox
    Then Click Create account button
#    Then Verify Join Target Circle page Opens # verify_text
##    Then Click Maybe Later button #click
##    Then Verify Target main page opens #verify_text

