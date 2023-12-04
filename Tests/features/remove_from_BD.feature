Feature: user can remove an element from the DB
    Scenario: user is removing an element from the DB 
    Given the user is on the home page
    When the user click the delete button
    Then the element is removed from the DB
    And the user is redirected to the home page
    And elements are updated in the table