# Created by HP at 6/30/2021
Feature: User can add shoes in the cart
  # Enter feature description here

  Scenario: User Add Shoes in the cart
    Given Open Amazon page
    When Search for shoes
    And click on the first product
    And click on Add to cart
    Then verify cart has 1 item