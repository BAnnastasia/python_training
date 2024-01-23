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

    def destroy(self):
        self.driver.quit()

    def return_home_page(self):
        with allure.step("Return home page"):
            self.driver.find_element(By.LINK_TEXT, "home page").click()


    def open_home_page(self):
        with allure.step("Open start page"):
            self.driver.get("http://mac-minik.local/addressbook/index.php")
