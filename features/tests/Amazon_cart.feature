# Created by HP at 6/27/2021
Feature: Test Amazon Cart


Scenario: User sees empty shopping cart
  Given:Open Amazon page
  When Click on cart icon
  Then "your Amazon Cart is empty" message is displayed

