Feature: Search for pets by category

As a pet shop customer
I need to be able to search for pets by category
So that I only see the pets that I'm interested in

Background:
    Given the following pets exist in the database
    | name  | category  | available |
    | Fido  | dog       | True      |
    | Kitty | cat       | True      |
    | Leo   | lion      | False     |

Scenario: Search for dogs
    Given I am on the "Home Page"
    When I set the "Category" to "dog"
    And I click the "Search" button
    Then I should see the message "Success"
    And I should see "Fido" in the results
    But I should not see "Kitty" in the results
    And I should not see "Leo" in the results
