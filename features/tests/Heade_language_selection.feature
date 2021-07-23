# Created by HP at 7/16/2021
Feature: Language selection tests

  Scenario: User can see Spanish language option
    Given Open Amazon page
    When Move mouse over flag icon
    Then Spanish language selection is visible

