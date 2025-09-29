from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    PATH = '/automation-practice-form'

    # локаторы
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    MOBILE = (By.CSS_SELECTOR, "#userNumber")

    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER = (By.CSS_SELECTOR, "label[for='gender-radio-3']")

    SUBMIT = (By.CSS_SELECTOR, "#submit")

    # модалка подтверждения
    RESULT_ROWS = (By.CSS_SELECTOR, "div.modal-content table tbody tr")

    # действия
    def open_form(self):
        self.open(self.PATH)

    def fill_forms(self, *, first: str, last: str, email: str, gender: str, mobile: str):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)

        gender = gender.strip().lower()
        mapping = {
            "male": self.GENDER_MALE,
            "female": self.GENDER_FEMALE,
            "other": self.GENDER_OTHER
        }

        if gender not in mapping:
            raise ValueError("gender must be one of: male, female or other")
        self.click(mapping[gender])

        self.type(self.MOBILE, mobile)

    def submit(self):
        try:
            self.driver.execute_script("document.getElementById('fixedban')?.remove();")
            self.driver.execute_script("document.getElementById('close-fixedban')?.click();")
        except Exception:
            pass

        btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()

    def result_ad_dict(self) -> dict:
        rows = self.wait.until(lambda d: d.find_elements(*self.RESULT_ROWS))
        data = {}
        for r in rows:
            tds = r.find_elements(By.TAG_NAME, "td")
            if len(tds) >= 2:
                key = tds[0].text.strip()
                val = tds[1].text.strip()
                if key:
                    data[key] = val
        return data