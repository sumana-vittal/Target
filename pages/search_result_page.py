import time
from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultPage(Page):

    SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")
    RIGHT_PANEL_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    RIGHT_PANEL_VIEW_CART_AND_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")
    RIGHT_PANEL_PRODUCT_NAME = (By.CSS_SELECTOR, "h4.styles_ndsHeading__HcGpD.styles_fontSize4__FN7fp.styles_x4Margin__JWxMT")
    RIGHT_PANEL_PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")

    def verify_search_product_result(self, search_text):
        self.verify_partial_text(search_text, *self.SEARCH_RESULT_HEADER)

    def verify_search_product_url(self, partial_url):
        self.verify_partial_url(partial_url)

    def click_add_to_cart(self):
        time.sleep(7)
        self.click(*self.ADD_TO_CART_BUTTON)

    def add_to_cart_in_right_panel(self):
        self.click(*self.RIGHT_PANEL_ADD_TO_CART)

    def click_view_cart_and_check_out(self):
        self.click(*self.RIGHT_PANEL_VIEW_CART_AND_CHECKOUT)

    def get_product_name(self):
        return self.get_text(*self.RIGHT_PANEL_PRODUCT_NAME)

    def get_product_price(self):
        return self.get_text(*self.RIGHT_PANEL_PRODUCT_PRICE)