Feature: OrangeHRM


  Scenario: Search Employee added or not
    Given I navigated to Login page
    When Click on Employee list
    And Search name in EmployeeList Searchbar
    Then Check employee added or not