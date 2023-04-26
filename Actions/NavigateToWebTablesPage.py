from typing import List
from selenium.webdriver.common.by import By
from screenplay import Actor, Action
from screenplay.interactions import Click, Clear, Enter, Wait

from Pages.HomePage import HomePage
from Pages.WebTablesPage import WebTablesPage


class NavigateToWebTablesPage(Action):
    def perform_as(self, actor: Actor) -> None:
        actor.attempts_to(
            Click.on(HomePage.elements),
            Click.on(WebTablesPage.web_tables),
            Wait.for_the_title(WebTablesPage.TITLE)
        )


class AddRowToWebTable(Action):
    def __init__(self, data: List[str]):
        self.data = data

    def perform_as(self, actor: Actor) -> None:
        actor.attempts_to(
            Click.on(WebTablesPage.add_new_record_button),
            *[Enter.the_value(data).into((By.XPATH, xpath)) for data, xpath in zip(self.data, WebTablesPage.form_fields)],
            Click.on(WebTablesPage.submit_button),
        )


class DeleteRowFromWebTable(Action):
    def __init__(self, row: int):
        self.row = row

    def perform_as(self, actor: Actor) -> None:
        row_locator = (By.XPATH, f"//div[@class='rt-tr-group'][{self.row}]//div[@class='rt-td'][1]")

        actor.attempts_to(
            Click.on((By.XPATH, f"//div[@class='rt-tr-group'][{self.row}]//span[@title='Delete']")),
            Wait.until_not_present(row_locator)
        )


def test_add_and_delete_row_on_web_tables():
    actor = Actor.named("User")

    actor.has(NavigateToWebTablesPage())

    data = ["John", "Doe", "johndoe@gmail.com", "35", "5000", "IT"]
    actor.attempts_to(AddRowToWebTable(data))

    row_to_delete = 1
    actor.attempts_to(DeleteRowFromWebTable(row_to_delete))
