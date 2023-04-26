from selenium.webdriver.common.by import By
from .BasePage import BasePage


class HomePage(BasePage):
    """Home page action methods come here"""

    # Web elements
    _logo = (By.XPATH, "//img[@src='/images/Toolsqa.jpg']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://demoqa.com/")

    def is_logo_displayed(self):
        return self.driver.find_element(*self._logo).is_displayed()

    def go_to_elements_page(self):
        elements_menu = self.driver.find_element(By.XPATH, "//div[@class='category-cards']//div[@class='card'][1]")
        elements_menu.click()

    def go_to_web_tables_page(self):
        elements_menu = self.driver.find_element(By.XPATH, "//div[@class='category-cards']//div[@class='card'][1]")
        elements_menu.click()
        web_tables_menu = self.driver.find_element(By.XPATH, "//li[@class='btn btn-light active'][contains(.,'Web Tables')]")
        web_tables_menu.click()
