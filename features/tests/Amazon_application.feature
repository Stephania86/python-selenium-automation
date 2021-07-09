# Created by HP at 7/5/2021
Feature: User Can Open and Close Amazon
 # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original window
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original


    Scenario: User can click on the 5 links
      Given Open Amazon Best Sellers page
      Then verify the each of the 5 top links open a new page
