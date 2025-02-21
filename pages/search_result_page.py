from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultPage(Page):

    SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")

    def verify_search_product_result(self, search_text):
        self.verify_partial_text(search_text, *self.SEARCH_RESULT_HEADER)

    def verify_search_product_url(self, partial_url):
        self.verify_partial_url(partial_url)
