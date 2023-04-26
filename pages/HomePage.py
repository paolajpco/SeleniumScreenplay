from selenium.webdriver.common.by import By
from .BasePage import BasePage


class HomePage(BasePage):
    ELEMENTS_BUTTON = (By.XPATH, "//div[@class='header-wrapper']//*[contains(text(),'Elements')]")

    def navigate_to_elements(self):
        self.click(self.ELEMENTS_BUTTON)
