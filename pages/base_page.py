from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f"Expected text '{expected_text}' not in actual '{actual_text}'"

    def verify_text(self, text, *locator):
        actual_text = self.find_element(*locator).text
        print(actual_text)
        assert text in actual_text, f"The search text {text} was not part of result."

    def verify_partial_url(self, partial_url_text):
        self.wait.until(
            EC.url_contains(partial_url_text),
            message=f"'{partial_url_text}' is not part of URL"
        )
