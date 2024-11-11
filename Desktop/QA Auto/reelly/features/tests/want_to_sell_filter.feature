Feature: Filter by "want to sell" option

  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open the main page https://soft.reelly.io/sign-in
    When Input rusmeister.spb@gmail.com as email
    And Input s@EB3kSAK@EQ3CK as password
    And Click "Continue"
    Then Click on “Secondary” option at the left side menu
    And Verify the right page opens
    And Click on Filters
    And Filter the products by “want to sell”
    And Click on Apply Filter
    And Verify all cards have “for sale” tag