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
            self.app.apply_value_str_by_name(driver, "group_name", group.name)
            self.app.apply_value_str_by_name(driver, "group_header", group.header)
            self.app.apply_value_str_by_name(driver, "group_footer", group.footer)
        with allure.step("Submit group creation"):
            driver.find_element(By.NAME, "submit").click()
            self.return_to_groups_page()



    def edit_first_group(self, group):
        driver = self.app.driver
        self.open_groups_page()
        with allure.step("Select a group"):
            driver.find_element(By.NAME, "selected[]").click()
        with allure.step("Edit a group"):
            driver.find_element(By.NAME, "edit").click()
            self.app.apply_value_str_by_name(driver, "group_name", group.name, True)
            self.app.apply_value_str_by_name(driver, "group_header", group.header, True)
            self.app.apply_value_str_by_name(driver, "group_footer", group.footer, True)
        with allure.step("Update group"):
            driver.find_element(By.NAME, "update").click()
            self.return_to_groups_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        with allure.step("Select a group"):
            driver.find_element(By.NAME,"selected[]").click()
        with allure.step("Delete a group"):
            driver.find_element(By.NAME,"delete").click()
        self.return_to_groups_page()


    def open_groups_page(self):
        driver = self.app.driver
        with allure.step("Open groups page"):
            driver.find_element(By.LINK_TEXT, "groups").click()

    def return_to_groups_page(self):
        driver = self.app.driver
        with allure.step("Return group page"):
            driver.find_element(By.LINK_TEXT, "group page").click()