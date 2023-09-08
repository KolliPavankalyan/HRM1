Feature: OrangeHRM

  Scenario: Add Employee details
    Given Click on Employee list
    When Enter all the details of employee
    And Saving details
    Then verifying Employee details added in database
