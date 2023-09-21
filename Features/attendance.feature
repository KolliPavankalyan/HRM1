Feature: OrangeHRM


  Scenario: Employee Punch In details
    Given I navigated to user Login page for attendance
    When I enter valid user email address and valid user password as into the fields
    And apply attendance punch in
    Then check employe punch in or not

  Scenario: Employee Punch Out details
    Given I navigated to user Login page for attendance
    When I enter valid user email address and valid user password as into the fields
    And apply attendance punch out
    Then check employe punch out or not