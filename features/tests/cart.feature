# Created by Ellen at 9/4/2024
Feature: Tests for Cart functionality

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown
