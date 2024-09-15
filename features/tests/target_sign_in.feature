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
    Then Verify Create account page form opened
    Then Input email on create account page
    And Input first name on create account page
    Then Input last name on create account page
    Then Input password on create account page
    And Click "Keep me signed in checkbox" on create account page
    Then Click Create account button
##    Then Verify Join Target Circle page Opens # verify_text
###    Then Click Maybe Later button #click
###    Then Verify Target main page opens #verify_text

  Scenario: User cannot login with wrong password
    Given Open target main page
    When Click Sign In
    When From right side navigation, click Sign in
    Then Verify Sign In form opened
    And Input email for sign-in
    Then Input incorrect password for sign-in
    And Click Sign in with password button
    Then Verify "That password is incorrect." message appears




