import allure
from pages.elements.web_table_page import WebTablePage

@allure.epic("DemoQA")
@allure.feature("Elements")
@allure.story("Web Tables")
@allure.severity(allure.severity_level.CRITICAL)
def test_webtables_add_and_find_record(browser):
    page = WebTablePage(browser)
    page.open_tables()

    data = {
        "first": "Brad",
        "last": "Pitt",
        "email": "bradPitt@mail.com",
        "age": 55,
        "salary": 120000,
        "departament": "actor"
    }

    page.click_add()
    page.fill_form(**data)
    page.submit_form()

    page.search(data["email"])
    assert page.row_count() == 1
    assert page.has_email_in_rows(data["email"])