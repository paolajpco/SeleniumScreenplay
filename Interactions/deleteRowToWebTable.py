from typing import List

from selenium.webdriver.common.by import By
from screenplay import Actor, Action
from screenplay.interactions import Click, Clear, Enter, Wait

from Pages.WebTablesPage import WebTablesPage


class DeleteRowFromWebTable(Action):
    def __init__(self, row_data: List[str]):
        self.row_data = row_data

    def perform_as(self, actor: Actor):
        # Open web tables page
        actor.attempts_to(NavigateToWebTablesPage())

        # Search for row to delete
        search_box = actor.ability_to(Wait).until_present(WebTablesPage.BUSCAR)
        actor.attempts_to(Enter(self.row_data[0], into=search_box))
        actor.attempts_to(Click(WebTablesPage.BTN_BUSCAR))

        # Verify row exists and select it for deletion
        row_xpath = f"//table/tbody/tr[td/a='{self.row_data[0]}'][td[text()='{self.row_data[1]}']]" \
                    f"[td[text()='{self.row_data[2]}']][td[text()='{self.row_data[3]}']]" \
                    f"[td[text()='{self.row_data[4]}']][td[text()='{self.row_data[5]}']]"
        row_checkbox = By.XPATH, f"{row_xpath}/td[1]/div/input"
        actor.ability_to(Wait).until_present(row_checkbox)
        actor.attempts_to(Click(row_checkbox))

        # Click delete button and confirm deletion
        actor.attempts_to(Click(WebTablesPage.BTN_DELETE))
        actor.ability_to(Wait).until_not_present(row_checkbox)
