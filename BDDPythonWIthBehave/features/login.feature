@pom_login
Feature: Login feature


  Scenario: Login with valid credentials
    Given I navigate to Login Page
    When I enter valid email and valid password into the fields
    And I click on Login button
    Then I should be successfully logged in


  Scenario: Login with invalid email and valid password
    Given I navigate to Login Page
    When I enter invalid email and valid password into the fields
    And I click on Login button
    Then I should get proper warning message


  Scenario: Login with valid email and invalid password
    Given I navigate to Login Page
    When I enter valid email and invalid password into the fields
    And I click on Login button
    Then I should get proper warning message


  Scenario: Login without entering any credential
    Given I navigate to Login Page
    When I don't enter anything into email and password fields
    And I click on Login button
    Then I should get proper warning message