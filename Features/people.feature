Feature: Jules people page

  Background:
    Given I am on people page

  @searchpeople

  Scenario Outline: Verify I can search people added to my account
    When I type "<name>" in search bar
    Then I see the "<results>" of the people I have on my account
    Examples:
      | name   | results      |
      | Maria  | Maria Stefan |
      | Stefan | Maria Stefan |

  @deletepeople

  Scenario: Delete people added to my account

    When I type a name in search bar
    And I select the first option and click delete
    Then I see the successfully delete confirmation

