# Created by raman at 2/20/25
Feature: Scenarios for the Home Page

  Scenario Outline: Search Product
    Given Open home page https://www.target.com/
    When Enter search keyword <search_query> in search textbox
    And Click on Search button
    Then Verify Product results for <result> are shown on search result page.
    Then Verify page URL has <search_query> in it.

    Examples:
    | search_query |  result  |
    |Watches       | Watches  |
    |Coffee        | Coffee   |
