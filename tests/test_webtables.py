from pytest_bdd import scenarios, given, when, then
from pages.HomePage import HomePage
from pages.WebTablePage import WebTablesPage
from actors.WebUser import WebUser
from utils import WebTablesConstants

scenarios("../features/webtables.feature", strict_gherkin=False)


@given("user on the web tables page")
def user_on_web_tables_page(browser):
    home_page = HomePage(browser)
    home_page.load()
    home_page.header.click_elements()
    home_page.header.click_web_tables()
    web_tables_page = WebTablesPage(browser)
    web_tables_page.wait_for_page_to_load()
    return web_tables_page


@when("user add a new record with the following data:")
def user_add_new_record(user_on_web_tables_page, table):
    first_name = table["First Name"]
    last_name = table["Last Name"]
    age = table["Age"]
    email = table["Email"]
    salary = table["Salary"]
    department = table["Department"]
    user_on_web_tables_page.click_add_new_record_button()
    user_on_web_tables_page.fill_new_record_form(
        first_name, last_name, age, email, salary, department
    )
    user_on_web_tables_page.click_submit_button()


@when('I get the record with name "<name>"')
def i_get_record_with_name(user_on_web_tables_page, name):
    user_on_web_tables_page.search(name)


@then("the record should be present in the table")
def record_should_be_present_in_table(user_on_web_tables_page):
    assert user_on_web_tables_page.is_record_present(
        WebTablesConstants.ADD_NEW_RECORD_FIRST_NAME,
        WebTablesConstants.ADD_NEW_RECORD_LAST_NAME,
        WebTablesConstants.ADD_NEW_RECORD_AGE,
        WebTablesConstants.ADD_NEW_RECORD_EMAIL,
        WebTablesConstants.ADD_NEW_RECORD_SALARY,
        WebTablesConstants.ADD_NEW_RECORD_DEPARTMENT,
    )


@when('I delete the record with name "<name>"')
def i_delete_record_with_name(user_on_web_tables_page, name):
    user_on_web_tables_page.delete_record(name)


@then("the record should not be present in the table")
def record_should_not_be_present_in_table(user_on_web_tables_page):
    assert not user_on_web_tables_page.is_record_present(
        WebTablesConstants.ADD_NEW_RECORD_FIRST_NAME,
        WebTablesConstants.ADD_NEW_RECORD_LAST_NAME,
        WebTablesConstants.ADD_NEW_RECORD_AGE,
        WebTablesConstants.ADD_NEW_RECORD_EMAIL,
        WebTablesConstants.ADD_NEW_RECORD_SALARY,
        WebTablesConstants.ADD_NEW_RECORD_DEPARTMENT,
    )
