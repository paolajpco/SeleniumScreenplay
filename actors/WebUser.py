from pages.BasePage import BasePage
from pages.HomePage import HomePage
from pages.WebTablePage import WebTablePage


class WebUser:
    def __init__(self, browser):
        self.browser = browser
        self.base_page = BasePage(self.browser)
        self.home_page = HomePage(self.browser)
        self.web_table_page = WebTablePage(self.browser)
