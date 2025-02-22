# Created by raman at 2/20/25
Feature: Scenario to test Product is added to cart.

  Scenario: Verify to add any Target’s product into the cart, and make sure it’s there
    Given Open home page https://www.target.com/
    When Enter search keyword coffee in search textbox
    And Click on Search button
    Then Verify Product results for coffee are shown on search result page.
    Then Verify page URL has coffee in it.
    When Click on Add to Cart
    And Click on Add to Cart in right panel
    And Click View cart and check out from right side panel
    Then verify it navigates to cart page
    And verify one product is added in the cart
    And verify price and product is same as added.