from pages.elements.radio_button_page import RadioButtonPage
import allure

@allure.epic("DemoQA")
@allure.feature("Elements")
@allure.story("radio button")
@allure.severity(allure.severity_level.CRITICAL)
def test_radio_button_yes(browser):
    page = RadioButtonPage(browser)
    page.open_radio()

    page.select_yes()

    assert "You have selected Yes" in page.result_text()

def test_radio_button_immersive(browser):
    page = RadioButtonPage(browser)
    page.open_radio()

    page.select_immersive()

    assert "You have selected Impressive" in page.result_text()