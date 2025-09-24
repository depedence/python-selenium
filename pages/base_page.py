from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовый слой: единые ожидания и элементарные действия"""

    def __init__(self, driver, base_url: str = "https://demoqa.com", timeout: int = 10):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path: str = '/'):
        """Открыть страницу: base_url + path"""

        url = self.base_url + ("" if path.startswith('/') else '/') + path
        self.driver.get(url)

    def click(self, locator):
        """Ждать кликабельность и кликнуть"""

        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text: str, clear: bool = True):
        """Ждать видимость, (опц.) очистить и ввести текст"""

        el = self.wait.until(EC.visibility_of_element_located(locator))

        if clear:
            el.clear()

        el.send_keys(text)

    def text_of(self, locator):
        """Ждать видимость и вернуть текст элемента"""

        return self.wait.until(EC.visibility_of_element_located(locator)).text