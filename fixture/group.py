import allure
from selenium.webdriver.common.by import By



class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        with allure.step("Init group creation"):
            driver.find_element(By.NAME, "new").click()
        with allure.step("Fill group form"):
            driver.find_element(By.NAME, "group_name").click()
            driver.find_element(By.NAME, "group_name").send_keys(group.name)
            driver.find_element(By.NAME, "group_header").click()
            driver.find_element(By.NAME, "group_header").send_keys(group.header)
            driver.find_element(By.NAME, "group_footer").click()
            driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        with allure.step("Submit group creation"):
            driver.find_element(By.NAME, "submit").click()
            self.return_to_groups_page()


    def open_groups_page(self):
        driver = self.app.driver
        with allure.step("Open groups page"):
            driver.find_element(By.LINK_TEXT, "groups").click()

    def return_to_groups_page(self):
        driver = self.app.driver
        with allure.step("Return group page"):
            driver.find_element(By.LINK_TEXT, "group page").click()