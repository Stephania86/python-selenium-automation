# Created by HP at 6/27/2021
Feature: Test Amazon Cart



  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for coffee mug
    And click on the first product
    And click on Add to cart button
    Then verify cart 1 item
