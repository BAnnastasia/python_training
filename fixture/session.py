import allure
from selenium.webdriver.common.by import By
class SessionHelper:
    def __init__(self, app):
        self.app = app
    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step("Login"):
            driver.find_element(By.NAME, "user").click()
            driver.find_element(By.NAME, "user").send_keys(username)
            driver.find_element(By.NAME, "pass").click()
            driver.find_element(By.NAME, "pass").send_keys(password)
            driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()
    def logout(self):
        driver = self.app.driver
        with allure.step("Logout"):
            driver.find_element(By.LINK_TEXT, "Logout").click()