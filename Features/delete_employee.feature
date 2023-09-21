Feature: OrangeHRM


  Scenario: Delete Employee from OrangeHRM Portal
    Given I navigated to Login page
    When Click on Employee list
    And Search name in EmployeeList Searchbar
    And Delete employee details
    Then Check employee added or not