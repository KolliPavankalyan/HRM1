Feature: OrangeHRM


  Scenario: Login with user Creditionals
    Given I navigated to Login page
    When I enter valid user email address and valid user password as into the fields
    And I click on user Login button
    Then I should user is get logged in or not
