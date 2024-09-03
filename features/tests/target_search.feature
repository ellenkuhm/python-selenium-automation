# Created by Ellen at 9/3/2024
Feature: Target main page search tests

  Scenario: User can search for a product on target
    Given Open target main page
    When Search for product
    Then Verify search worked