from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    PATH = '/text-box'

    # локаторы
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT = (By.ID, "currentAddress")
    PERMANENT = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")

    OUT_NAME = (By.ID, "name")
    OUT_EMAIL = (By.ID, "email")

    # навигация
    def open_text_box(self):
        self.open(self.PATH)

    # действия
    def fill_form(self, name: str, email: str, current_addr: str, perm_addr: str):
        self.type(self.FULL_NAME, name)
        self.type(self.EMAIL, email)
        self.type(self.CURRENT, current_addr)
        self.type(self.PERMANENT, perm_addr)

    def submit(self):
        self.click(self.SUBMIT)

    # чтение результатов
    def output_name(self) -> str:
        return self.text_of(self.OUT_NAME)

    def output_email(self) -> str:
        return self.text_of(self.OUT_EMAIL)