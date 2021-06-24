# Created by HP at 6/24/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario:  Open Amazon page
    Given Open the Amazon page
    When click on the cart section
    Then verify cart value is 0
