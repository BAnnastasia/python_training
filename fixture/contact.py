import allure
from selenium.webdriver.common.by import By
class ContactHelper:
    def __init__(self,app):
        self.app = app
    def open_new_contact_page(self):
        driver = self.app.driver
        with allure.step("Open add new contact page"):
            driver.find_element(By.LINK_TEXT, "add new").click()

    def fild_contact_form(self, contact, clear=False):
        driver = self.app.driver
        with allure.step("Fill contact form"):
            self.app.apply_value_str_by_name(driver, "firstname", contact.firstname, clear)
            self.app.apply_value_str_by_name(driver, "lastname", contact.lastname, clear)
            self.app.apply_value_str_by_name(driver, "address", contact.address, clear)
            self.app.apply_value_str_by_name(driver, "email", contact.email, clear)
            self.app.apply_value_str_by_name(driver, "byear", contact.byear, clear)
            self.app.apply_value_dropdown_by_name(driver, "bmonth", contact.bmonth)  # dropdown
            self.app.apply_value_dropdown_by_name(driver, "bday", contact.bday)  # dropdown
            self.app.apply_value_str_by_name(driver, "mobile", contact.mobile, clear)
            self.app.apply_value_str_by_name(driver, "homepage", contact.homepage, clear)

            self.app.apply_value_str_by_name(driver, "middlename", contact.middlename, clear)
            self.app.apply_value_str_by_name(driver, "nickname", contact.nickname, clear)
            self.app.apply_value_str_by_name(driver, "photo", contact.photo, clear)
            self.app.apply_value_str_by_name(driver, "delete", contact.delete, clear)
            self.app.apply_value_str_by_name(driver, "company", contact.company, clear)
            self.app.apply_value_str_by_name(driver, "title", contact.title, clear)
            self.app.apply_value_str_by_name(driver, "home", contact.home, clear)
            self.app.apply_value_str_by_name(driver, "work", contact.work, clear)
            self.app.apply_value_str_by_name(driver, "fax", contact.fax, clear)
            self.app.apply_value_str_by_name(driver, "email2", contact.email2, clear)
            self.app.apply_value_str_by_name(driver, "email3", contact.email3, clear)
            self.app.apply_value_str_by_name(driver, "aday", contact.aday)  # dropdown
            self.app.apply_value_str_by_name(driver, "amonth", contact.amonth)  # dropdown
            self.app.apply_value_str_by_name(driver, "ayear", contact.ayear, clear)
            self.app.apply_value_str_by_name(driver, "new_group", contact.new_group, clear)
            self.app.apply_value_str_by_name(driver, "address2", contact.address2, clear)
            self.app.apply_value_str_by_name(driver, "phone2", contact.phone2, clear)
            self.app.apply_value_str_by_name(driver, "notes", contact.notes, clear)


    def create(self, contact):
        driver = self.app.driver
        self.open_new_contact_page()
        self.fild_contact_form(contact)
        with allure.step("Submit contact creation"):
            driver.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()

    def edit_first_contact(self,contact):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step("Select a contact"):
            driver.find_element(By.NAME, "selected[]").click()
        with allure.step("Edit contact"):
            driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
            self.fild_contact_form(contact, True)
        with allure.step("Update contact"):
            driver.find_element(By.NAME, "update").click()

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements(By.NAME,"selected[]"))

    def delete_first_contact(self):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step("Select a contact"):
            driver.find_element(By.NAME, "selected[]").click()
        with allure.step("Delete a contact"):
            driver.find_element(By.XPATH,"//input[@value='Delete']").click()