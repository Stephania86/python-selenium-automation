# Created by HP at 7/17/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select Books Department
    And Search for faust
    Then Verify books department is selected