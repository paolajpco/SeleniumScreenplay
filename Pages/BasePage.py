from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demoqa.com/"
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def wait_for_element_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickability(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open(self):
        self.driver.get(self.base_url)

    def scroll_to_element(self, element):
        self.actions.move_to_element(element).perform()

    def send_keys(self, element, keys):
        self.wait_for_element_visibility(element)
        element.send_keys(keys)

    def click(self, element):
        self.wait_for_element_clickability(element)
        element.click()

    def clear(self, element):
        self.wait_for_element_visibility(element)
        element.clear()

    def press_enter(self):
        self.actions.send_keys(Keys.ENTER).perform()
