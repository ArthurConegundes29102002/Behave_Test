Feature: user can add an element in the DB
    Scenario: user is adding an element into DB
        Given the user is on the home page
        When the user submits the form
        Then the element is added in the DB
        And the user is redirected to the home page
        And elements are updated in the table




