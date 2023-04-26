from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def visit(self, url):
        self.browser.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def type(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()
