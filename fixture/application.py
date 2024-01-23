from selenium import webdriver
import allure
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def destroy(self):
        self.driver.quit()

    def logout(self):
        with allure.step("Logout"):
            self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        with allure.step("Return group page"):
            self.driver.find_element(By.LINK_TEXT, "group page").click()

    def return_home_page(self):
        with allure.step("Return home page"):
            self.driver.find_element(By.LINK_TEXT, "home page").click()

    def create_group(self, group):
        self.open_groups_page()
        with allure.step("Init group creation"):
            self.driver.find_element(By.NAME, "new").click()
        with allure.step("Fill group form"):
            self.driver.find_element(By.NAME, "group_name").click()
            self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
            self.driver.find_element(By.NAME, "group_header").click()
            self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
            self.driver.find_element(By.NAME, "group_footer").click()
            self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        with allure.step("Submit group creation"):
            self.driver.find_element(By.NAME, "submit").click()
            self.return_to_groups_page()

    def open_groups_page(self):
        with allure.step("Open groups page"):
            self.driver.find_element(By.LINK_TEXT, "groups").click()

    def open_contact_page(self):
        with allure.step("Open contact page"):
            self.driver.find_element(By.LINK_TEXT, "add new").click()

    def create_contact(self, contact):
        self.open_contact_page()
        with allure.step("Fill contact form"):
            self.driver.find_element(By.NAME, "firstname").click()
            self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
            self.driver.find_element(By.NAME, "lastname").click()
            self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
            self.driver.find_element(By.NAME, "address").click()
            self.driver.find_element(By.NAME, "address").send_keys(contact.address)
            self.driver.find_element(By.NAME, "email").click()
            self.driver.find_element(By.NAME, "email").send_keys(contact.email)
            self.driver.find_element(By.NAME, "byear").click()
            self.driver.find_element(By.NAME, "byear").send_keys(contact.byear)
            self.driver.find_element(By.NAME, "bmonth").click()
            dropdown = self.driver.find_element(By.NAME, "bmonth")
            dropdown.find_element(By.XPATH, f"//option[. = '{contact.bmonth}']").click()
            self.driver.find_element(By.NAME, "bday").click()
            dropdown = self.driver.find_element(By.NAME, "bday")
            if contact.bday.isdigit():
                dropdown.find_element(By.XPATH, f"//option[. = '{int(contact.bday)}']").click()
            else:
                dropdown.find_element(By.XPATH, f"//option[. = '{contact.bday}']").click()
            self.driver.find_element(By.NAME, "mobile").click()
            self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
            self.driver.find_element(By.NAME, "homepage").click()
            self.driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        with allure.step("Submit contact creation"):
            self.driver.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()

    def login(self, username, password):
        self.open_home_page()
        with allure.step("Login"):
            self.driver.find_element(By.NAME, "user").click()
            self.driver.find_element(By.NAME, "user").send_keys(username)
            self.driver.find_element(By.NAME, "pass").click()
            self.driver.find_element(By.NAME, "pass").send_keys(password)
            self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()

    def open_home_page(self):
        with allure.step("Open home page"):
            self.driver.get("http://mac-minik.local/addressbook/index.php")
