import allure
from selenium.webdriver.common.by import By
from model.group import Group



class GroupHelper:
    def __init__(self, app):
        self.app = app

    def fild_group_form(self,group):
        driver = self.app.driver
        with allure.step("Fill group form"):
            self.app.apply_value_str_by_name(driver, "group_name", group.name)
            self.app.apply_value_str_by_name(driver, "group_header", group.header)
            self.app.apply_value_str_by_name(driver, "group_footer", group.footer)

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        with allure.step("Init group creation"):
            driver.find_element(By.NAME, "new").click()
        self.fild_group_form(group)
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
            self.fild_group_form(group)
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
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements(By.NAME,"new")) > 0):
            with allure.step("Open groups page"):
                driver.find_element(By.LINK_TEXT, "groups").click()

    def return_to_groups_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements(By.NAME, "new")) > 0):
            with allure.step("Return group page"):
                driver.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements(By.NAME,"selected[]"))
    def get_group_list(self):
        driver = self.app.driver
        self.open_groups_page()
        groups = []

        for element in driver.find_elements(By.CSS_SELECTOR,"span.group"):
            name = element.text
            id = element.find_element(By.NAME,"selected[]").get_attribute("value")
            groups.append(Group(name=name, id=id))
        return groups



