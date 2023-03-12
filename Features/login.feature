Feature: Jules Login


  Scenario: Login with valid credentials
    Given I am on the login page
    When I input a valid email and a valid password
    And I click the login button
    Then I see my account

  Scenario: Logout Jules Account
      Given I am on my account page
      When I click my account options
      And I select logout
      Then I see the login page

  Scenario: Login with invalid email and valid password
    Given I am on the login page
    When I input invalid email and valid password
    And I click the login button
    Then I am still on the sign-in page

  Scenario: Login with valid email and invalid password
    Given I am on the login page
    When I input valid email with invalid password
    And I click the login button
    Then I am still on the sign-in page

  Scenario: Login with invalid credentials
    Given I am on the login page
    When I input invalid credentials
    And I click the login button
    Then I am still on the sign-in page