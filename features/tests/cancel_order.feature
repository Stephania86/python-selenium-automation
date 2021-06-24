# Created by HP at 6/23/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: search for cancelling an order and verify the page is open
    Given Open Amazon help page
    When type cancel order in the search field
    Then verify sign in page works
