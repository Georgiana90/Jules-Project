Feature: Jules Add page

  Scenario: Add people to personal account
    Given I am on Jules Add page
    When I select the option to add person
    And I input firstname and lastname
    And I click save button
    Then I see the confirmation message

  Scenario: Add people to account using numbers
    Given I am on Jules Add page
    When I select the option to add person
    And I input numbers in firstname and lastname
    Then I see the error message







