from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class WebTablesPage(BasePage):

    # Web Tables Page locators
    web_tables_button = (By.XPATH, "//li[@class='btn btn-light active'][contains(.,'Web Tables')]")
    add_button = (By.XPATH, "//button[contains(@id,'addNewRecordButton')]")
    title = (By.XPATH, "//div[@class='main-header'][contains(.,'Web Tables')]")
    first_name_input = (By.XPATH, "//input[contains(@id,'firstName')]")
    last_name_input = (By.XPATH, "//input[contains(@id,'lastName')]")
    email_input = (By.XPATH, "//input[contains(@id,'userEmail')]")
    age_input = (By.XPATH, "//input[contains(@id,'age')]")
    salary_input = (By.XPATH, "//input[contains(@id,'salary')]")
    department_input = (By.XPATH, "//input[contains(@id,'department')]")
    submit_button = (By.XPATH, "//button[contains(@id,'submit')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_web_tables(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.web_tables_button)).click()

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.add_button)).click()

    def fill_form(self, first_name, last_name, email, age, salary, department):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.age_input).send_keys(age)
        self.driver.find_element(*self.salary_input).send_keys(salary)
        self.driver.find_element(*self.department_input).send_keys(department)

    def click_submit_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.submit_button)).click()
