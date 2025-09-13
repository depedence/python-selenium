from selenium.webdriver.common.by import By
import time

def test_fill_text_box_forms(browser):
    browser.get("https://demoqa.com/")

    card_elements = browser.find_element(By.CLASS_NAME, "card-up")
    card_elements.click()
    time.sleep(1)

    textbox = browser.find_element(By.ID, "item-0")
    textbox.click()
    time.sleep(1)

    fullname_input = browser.find_element(By.ID, "userName")
    fullname_input.send_keys("my full name")
    time.sleep(1)

    email_input = browser.find_element(By.ID, "userEmail")
    email_input.send_keys("example@mail.com")
    time.sleep(1)

    currentAddress_input = browser.find_element(By.ID, "currentAddress")
    currentAddress_input.send_keys("Moscow City")
    time.sleep(1)

    permanentAddress_input = browser.find_element(By.ID, "permanentAddress")
    permanentAddress_input.send_keys("St. Petersburg")
    time.sleep(1)

    submit_btn = browser.find_element(By.ID, "submit")
    submit_btn.click()
    time.sleep(5)