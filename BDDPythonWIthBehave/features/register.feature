Feature: User Registration

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter details into mandatory fields
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with all fields
    Given I navigate to Register Page
    When I enter details into all fields
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  @register_duplicate
  Scenario: Register with a duplicate email address
    Given I navigate to Register Page
    When I enter details into all fields except email field
    And I enter existing accounts email into email field
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning message informing about duplicate account should be displayed

  @empty
  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper warning messages for every mandatory fields should be displayed
