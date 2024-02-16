Feature: Search Functionality

  @search @pom
  Scenario: Search for a valid product
    Given I am on HomePage
    When I enter a valid product into the Search box field
    And I click on Search button
    Then Valid product should get displayed in Search results

  @search @pom
  Scenario: Search for a invalid product
    Given I am on HomePage
    When I enter invalid product into the Search box field
    And I click on Search button
    Then Proper message should be displayed in Search Results

  @search @pom
  Scenario: Search without entering a product
    Given I am on HomePage
    When I don't enter anything into the Search box field
    And I click on Search button
    Then Proper message should be displayed in Search Results


