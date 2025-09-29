from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RadioButtonPage(BasePage):
    PATH = '/radio-button'

    # локаторы
    YES = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMMERSIVE = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    RESULT = (By.CSS_SELECTOR, "p.mt-3")

    # навигация
    def open_radio(self):
        self.open(self.PATH)

    # действия
    def select_yes(self):
        self.click(self.YES)

    def select_immersive(self):
        self.click(self.IMMERSIVE)

    def result_text(self) -> str:
        return self.text_of(self.RESULT)