from selenium.webdriver.common.by import By

from pages.base_page import Page


class HomePage(Page):

    SEARCH_TEXTBOX = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

    def open_home_page(self, url):
        self.open_url(url)

    def enter_search_text(self, search_text):
        self.input_text(search_text, *self.SEARCH_TEXTBOX)

    def click_search_button(self):
        self.click(*self.SEARCH_BUTTON)








