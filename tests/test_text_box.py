import allure
from pages.elements.text_box_page import TextBoxPage

@allure.epic("DemoQA")
@allure.feature("Elements")
@allure.story("text box")
@allure.severity(allure.severity_level.CRITICAL)
def test_text_box(browser):
    page = TextBoxPage(browser)
    page.open_text_box()

    page.fill_form(
        name='my full name',
        email='example@mail.com',
        current_addr='Moscow City',
        perm_addr='St. Petersburg'
    )

    page.submit()

    assert 'my full name' in page.output_name()
    assert 'example@mail.com' in page.output_email()