# Created by Ellen at 9/13/2024
Feature: Tests for Help page

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened


#  Scenario: User can select Help topic Target Circle
#    Given Open Help page for Returns
#    Then Verify help Returns page opened
#    When Select Help topic Delivery & Pickup
#    Then Verify help Drive Up & Order Pickup page opened