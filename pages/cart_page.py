from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):

    CART_PRODUCT_PRICE_LABEL = (By.CSS_SELECTOR, ".sc-93ec7147-3")
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR,"div.styles_mdHiddenDown__MPUqz [data-test='cartItem-price']")

    def verify_cart_page(self):
        self.verify_partial_url("cart")

    def verify_product_added_to_cart(self):
        product_details = self.get_text(*self.CART_PRODUCT_PRICE_LABEL)
        print(product_details)

    def verify_price_and_product_is_right(self, product_name, product_price):
        self.verify_text(product_name, *self.CART_PRODUCT_NAME)
        self.verify_text(product_price, *self.CART_PRODUCT_PRICE)
