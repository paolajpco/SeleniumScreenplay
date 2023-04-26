from behave import given, when, then
from pages.WebTablePage import WebTablePage
from hamcrest import assert_that, equal_to


@given("user on the web tables page")
def step_impl(context):
    context.web_tables_page = WebTablesPage(context.driver)
    context.web_tables_page.load()


@when("user add a new record with the following data")
def step_impl(context):
    table_data = context.table[1]  # Get data row from table (skip header)
    context.web_tables_page.add_record(*table_data)


@when("I get the record with name {name}")
def step_impl(context, name):
    context.record_data = context.web_tables_page.get_record_by_name(name)


@then("the record should be present in the table")
def step_impl(context):
    assert_that(context.record_data, equal_to(context.table[1].as_dict()))


@when("I delete the record with name {name}")
def step_impl(context, name):
    context.web_tables_page.delete_record_by_name(name)


@then("the record should not be present in the table")
def step_impl(context):
    assert_that(context.web_tables_page.record_exists(context.record_data), equal_to(False))
