# Created by HP at 7/5/2021
Feature: Tests for 404 page
  # Enter feature description here

  Scenario: 404 page tales to Amazon Blog
    Given Open Amazon Product INVALID_B081YS2F7N page
    When store original Window
    When Click on the dog image
    When Switch to the new window
    Then Verify Amazon Blog url
    Then close new Window
    When Return to original Window
    Then Verify Amazon url