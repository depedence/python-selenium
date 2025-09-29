import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# вложения при падении теста
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            try:
                png = driver.get_screenshot_as_png()
                allure.attach(png, name="screenshot", attachment_type=AttachmentType.PNG)
            except Exception:
                pass
            try:
                html = driver.page_source
                allure.attach(html, name="page_source", attachment_type=AttachmentType.HTML)
            except Exception:
                pass
