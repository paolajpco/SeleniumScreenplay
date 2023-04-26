from typing import List
from selenium.webdriver.common.by import By
from screenplay import Actor, Action
from screenplay.interactions import Click, Clear, Enter, Wait

from Pages.HomePage import HomePage
from Pages.WebTablesPage import WebTablesPage


class AddRowToWebTable(Action):
    def __init__(self, data: List[str]):
        self.data = data

    def perform_as(self, actor: Actor) -> None:
        actor.attempts_to(
            Click.on(HomePage.elements),
            Click.on(WebTablesPage.web_tables),
            Click.on(WebTablesPage.add_new_record_button),
            *[Enter.the_value(data).into((By.XPATH, xpath)) for data, xpath in zip(self.data, WebTablesPage.form_fields)],
            Click.on(WebTablesPage.submit_button),
        )
