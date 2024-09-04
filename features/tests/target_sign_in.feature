# Created by Ellen at 9/4/2024
Feature: Log-in Functionality

  Scenario: User can sign-in after being logged out
    Given Open target main page
    When Click Sign In
    When From right side navigation, click Sign in
    Then Verify Sign In form opened