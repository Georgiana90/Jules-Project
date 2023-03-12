Feature: Jules people page

  Scenario: Search people added to my account by firstname
    Given I am logged in my Jules account
    When I select people option
    And I type the firstname in search bar
    Then I see the results of the people I have on my account

  Scenario: Search people added to my account by lastname
    Given I am on people page
    When I type the lastname in search bar
    Then I see the results of the people I have on my account

  Scenario: Delete people added to my account
    Given I am on people page
    When I type a name in search bar
    And I select the first option and click delete
    Then I see the successfully delete confirmation

