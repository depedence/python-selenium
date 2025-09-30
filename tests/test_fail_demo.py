import pytest
import allure

@allure.epic("DemoQA")
@allure.feature("Demo")
@allure.story("Fail example")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.ui
def test_demo_fail(browser):
    """Демонстрационный тест, который заведомо падает"""
    browser.get("https://demoqa.com/text-box")
    # проверка, которая точно не выполнится
    assert "SomeWrongText" in browser.page_source