Feature: Jules Add page

  Background:
    Given I am on Jules Add page
    When I select the option to add person

  @addpeoplesuccessfully

  Scenario: Add people to personal account

    When I input firstname and lastname
    And I click save button
    Then I see the confirmation message

  @failaddingpeople

  Scenario Outline: Check add people to my account option using digits and symbols

    When I type "<firstname>" and "<lastname>"
    Then I see the "<error_message>"
    Examples:
      | firstname | lastname  | error_message       |
      | 48397943  | 45397543  | invalid field value |
      | #@Maria   | !"Stefan£ | invalid field value |







