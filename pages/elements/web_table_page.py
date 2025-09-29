from operator import truediv

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WebTablePage(BasePage):
    PATH = '/webtables'

    # кнопки и поля формы добавления/редактирования
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    SUBMIT = (By.CSS_SELECTOR, "#submit")

    # поля модальной формы
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    AGE = (By.CSS_SELECTOR, "#age")
    SALARY = (By.CSS_SELECTOR, "#salary")
    DEPARTAMENT = (By.CSS_SELECTOR, "#department")

    # поиск и таблица
    SEARCH = (By.CSS_SELECTOR, "#searchBox")
    ROWS = (By.CSS_SELECTOR, "div.rt-tbody div.rt-tr-group")
    NO_DATA = (By.CSS_SELECTOR, "div.rt-noData")

    def open_tables(self):
        self.open(self.PATH)

    def click_add(self):
        self.click(self.ADD_BUTTON)

    def fill_form(self, *, first, last, email, age, salary, departament):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)
        self.type(self.AGE, str(age))
        self.type(self.SALARY, str(salary))
        self.type(self.DEPARTAMENT, departament)

    def submit_form(self):
        self.click(self.SUBMIT)

    # поиск / чтение таблиц
    def search(self, text: str):
        self.type(self.SEARCH, text)

    def visible_rows_text(self):
        # возвращаем тексты видимых строк
        rows = self.driver.find_elements(*self.ROWS)
        texts = []

        for r in rows:
            txt = r.text.strip()
            if txt: # пустые группы отбрасываем
                texts.append(txt)

        return texts

    def row_count(self) -> int:
        return len(self.visible_rows_text())

    def has_email_in_rows(self, email: str) -> bool:
        return any(email in t for t in self.visible_rows_text())

    # действия по строке
    def delete_first_visible_row(self):
        rows = self.driver.find_elements(*self.ROWS)

        for r in rows:
            if r.text.strip():
                delete_btn = r.find_element(By.CSS_SELECTOR, "span[title='Delete']")
                delete_btn.click()

                return True

        return False

    def edit_first_visible_row(self, *, first=None, last=None, email=None, age=None, salary=None, departament=None):
        rows = self.driver.find_elements(*self.ROWS)

        for r in rows:
            if r.text.strip():
                r.find_element(By.CSS_SELECTOR, "span[title='Edit']").click()
                if first is not None:  self.type(self.FIRST_NAME, first)
                if last is not None:  self.type(self.LAST_NAME, last)
                if email is not None:  self.type(self.EMAIL, email)
                if age is not None:  self.type(self.AGE, str(age))
                if salary is not None: self.type(self.SALARY, str(salary))
                if departament is not None:  self.type(self.DEPARTAMENT, departament)

                self.submit_form()

                return True

        return False