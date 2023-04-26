from screenpy import BrowseTheWeb
from screenpy import Target
from selenium.webdriver.common.by import By


class HomePage:
    URL = "https://demoqa.com/"
    LOGO = Target.the("logo").located(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")

    @staticmethod
    def visit():
        BrowseTheWeb.as_user().to(HomePage.URL)
