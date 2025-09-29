import allure
from pages.forms.practice_form_page import PracticeFormPage

@allure.epic("DemoQA")
@allure.feature("Elements")
@allure.story("Web Tables")
@allure.severity(allure.severity_level.CRITICAL)
def test_practice_form_minimal_happy_path(browser):
    page = PracticeFormPage(browser)
    page.open_form()

    data = {
        "first": "John",
        "last": "QA",
        "email": "john.qa@example.com",
        "gender": "male",  # допустимо: male/female/other
        "mobile": "9876543210",  # важно: ровно 10 цифр
    }

    page.fill_forms(**data)
    page.submit()

    result = page.result_ad_dict()

    assert result.get("Student Name") == f"{data['first']} {data['last']}"
    assert result.get("Student Email") == data["email"]
    assert result.get("Gender") == "Male"
    assert result.get("Mobile") == data["mobile"]