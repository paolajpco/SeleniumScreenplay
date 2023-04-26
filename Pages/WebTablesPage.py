from selenium.webdriver.common.by import By
from setuptools.config.setupcfg import Target


class WebTablesPage:
    URL = "https://demoqa.com/webtables"
    WEB_TABLES = Target.the("Web Tables").located(By.XPATH, "//li[@class='btn btn-light active'][contains(.,'Web Tables')]")
    TITLE = Target.the("Title").located(By.XPATH, "//div[@class='main-header'][contains(.,'Web Tables')]")
    ADD_BUTTON = Target.the("Add Button").located(By.XPATH, "//button[contains(@id,'addNewRecordButton')]")
    SEARCH_BOX = Target.the("Search Box").located(By.XPATH, "//input[contains(@id,'searchBox')]")
    SEARCH_BUTTON = Target.the("Search Button").located(By.XPATH, "//svg[contains(@stroke,'currentColor')]")
    DELETE_BUTTON = Target.the("Delete Button").located(By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[7]/div")
