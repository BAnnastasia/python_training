from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()


    def open_home_page(self):
        driver = self.driver
        if not (driver.current_url.endswith("/index.php") and len(driver.find_elements(By.XPATH, "//input[@value='Send e-Mail']")) > 0):
            with allure.step("Open start page"):
                self.driver.get("http://mac-minik.local/addressbook/index.php")

    @staticmethod
    def apply_value_str_by_name(driver, field_name, value, clear=False):
        if value is None:
            return
        element = driver.find_element(By.NAME, field_name)
        if clear:
            element.clear()
        element.click()
        element.send_keys(value)

    @staticmethod
    def apply_value_dropdown_by_name(driver, dropdown_name, value):
        if value is None:
            return
        driver.find_element(By.NAME, dropdown_name).click()
        dropdown = driver.find_element(By.NAME, dropdown_name)
        dropdown.find_element(By.XPATH, f"//option[. = '{value}']").click()