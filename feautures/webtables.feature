Feature: CRUD operations on web tables

  Scenario: Add, get, and delete a record from a web table
    Given user on the web tables page
    When user add a new record with the following data:
      | First Name  |Last Name  | Age  | Email  |Salary |Department |
      | testt       |ttttt      |22    |test    |1000   |Bogota     |
    And I get the record with name "Paola"
    Then the record should be present in the table
    When I delete the record with name "Paola"
    Then the record should not be present in the table
