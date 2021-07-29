# Created by HP at 6/23/2021
Feature: Test scenario for sign in page


  Scenario: click on orders and verify sign in page is open
    Given Open Amazon page
    When Click orders
    Then verify sign page opened


  Scenario: Sign in page can be opened from Sing In popup
      Given Open the Amazon page
      When Click Sign In from popup
      Then Verify Sign In page is opened


  Scenario: User can select all colors
      Given Open Amazon Product B081YS2F7N page
      Then Verify user can click through colors


  Scenario: click on orders and verify sign in page is open
    Given Open Amazon page
    Then Verify Sign in popup is clickable
    When wait for 5 sec
    Then Verify Sign in popup is clickable
    Then verify sign in popup disappears


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened

  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify "Your Shopping Cart is empty" message is displayed


  Scenario: Open Amazon page and search for an item
    Given Open the Amazon page
    When Search for coffee mug
    And click on the first product
    When click on Add to cart button
    Then verify cart has 1 item

