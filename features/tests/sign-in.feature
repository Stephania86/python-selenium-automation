Feature: test for sign in page

    Scenario logged out user sees Sign in page when clicking Orders
      Given Open Amazon page
      When Click orders Then verify sign page opened


    Scenario: Sign in page can be opened from Sing In popup
      Given Open Amazon page
      When Click Sign In from popup
      Then Verify Sign In page opened


    Scenario: User can select all colors
      Given Open Amazon Product B081YS2F7N page
      Then Verify user can click through colors

