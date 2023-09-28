Feature: OrangeHRM


  Scenario: Employee leave
    Given Log into dashboard page
    When enter into leave page
    And apply leave in leave page
    And login to admin page and approved leave
    Then check status of leave