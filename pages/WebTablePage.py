from selenium.webdriver.common.by import By
from .BasePage import BasePage


class WebTablePage(BasePage):
    WEB_TABLES_BUTTON = (By.XPATH, "//li[@class='btn btn-light active']//*[contains(text(),'Web Tables')]")
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    SEARCH_BOX = (By.ID, "searchBox")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='searchBox']//*[local-name()='svg']")
    DELETE_BUTTON = (By.XPATH, "//div[@id='delete-record-undefined']//*[local-name()='svg']")

    def navigate_to_web_tables(self):
        self.click(self.WEB_TABLES_BUTTON)

    def add_new_record(self, first_name, last_name, age, email, salary, department):
        self.click(self.ADD_BUTTON)
        self.type((By.ID, "firstName"), first_name)
        self.type((By.ID, "lastName"), last_name)
        self.type((By.ID, "userEmail"), email)
        self.type((By.ID, "age"), age)
        self.type((By.ID, "salary"), salary)
        self.type((By.ID, "department"), department)
        self.click((By.ID, "submit"))

    def search_record(self, text):
        self.type(self.SEARCH_BOX, text)
        self
