Feature: Jules Login

  Background:
    Given I am on the login page

  @JulesLogin @invalidLogin

  Scenario Outline: Verify I cannot login in my Jules account with invalid credentials
    When I insert "<username>" and "<password>"
    And I click the login button
    Then I cannot login to my account and see the "<error_msg>"

    Examples:
      | username                      | password     | error_msg                          |
      | georgianabanciu@gmail.com     | Test123test! | Invalid email/password combination |
      | georgianabanciu1511@gmail.com | TestTest     | Invalid email/password combination |
      | georgianabanciu@gmail.com     | TestTest     | Invalid email/password combination |

  @successfulLogin

  Scenario: Verify I can login in my Jules account with valid credentials

    When I input a valid email and a valid password
    And I click the login button
    Then I see my Jules account

