from pages.base_page import Page
from pages.home_page import HomePage
from pages.search_result_page import SearchResultPage


class Application:

    def __init__(self, driver):
        self.driver = Page(driver)
        self.home_page = HomePage(driver)
        self.search_result_page = SearchResultPage(driver)
