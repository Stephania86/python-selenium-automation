# Created by HP at 6/11/2021
Feature: Test Amazon search
  # Enter feature description here

  Scenario: User can search for a product
    Given Open  Amazon  page
    When Input Table in search field
    And click on Amazon search icon
    Then verify search worked for Table


     Scenario: Amazon footer has correct amount of links
      Given Open  Amazon  page
       Then verify 40 footer links are displayed