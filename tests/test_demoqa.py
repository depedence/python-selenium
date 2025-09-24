from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_fill_text_box_forms(browser):
    browser.get("https://demoqa.com/")
    wait = WebDriverWait(browser, 10)

    elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]")))
    elements_card.click()

    textbox_menu = wait.until(EC.element_to_be_clickable((By.ID, "item-0")))
    textbox_menu.click()

    wait.until(EC.visibility_of_element_located((By.ID, "userName"))).send_keys("my full name")
    wait.until(EC.visibility_of_element_located((By.ID, "userEmail"))).send_keys("example@mail.com")
    wait.until(EC.visibility_of_element_located((By.ID, "currentAddress"))).send_keys("Moscow City")
    wait.until(EC.visibility_of_element_located((By.ID, "permanentAddress"))).send_keys("St. Petersburg")

    wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

    assert "my full name" in wait.until(EC.visibility_of_element_located((By.ID, "name"))).text
    assert "example@mail.com" in wait.until(EC.visibility_of_element_located((By.ID, "email"))).text