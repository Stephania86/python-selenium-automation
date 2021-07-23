# Created by HP at 6/28/2021
Feature: Open Amazon Best seller Page then verify there are 3 links
  # Enter feature description here


    Scenario:  User can see the Best sellers link
      Given Open Amazon Best Sellers page
      Then Verify that are 5 links

       Scenario: Bestsellers links can be opened
         Given Open Amazon Best Sellers page
         Then User can click through top links and verify correct page opens


