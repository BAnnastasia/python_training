import allure
from selenium.webdriver.common.by import By
class ContactHelper:
    def __init__(self,app):
        self.app = app
    def open_new_contact_page(self):
        driver = self.app.driver
        with allure.step("Open add new contact page"):
            driver.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contact):
        driver = self.app.driver
        self.open_new_contact_page()
        with allure.step("Fill contact form"):
            self.app.apply_value_str_by_name(driver, "firstname", contact.firstname)
            self.app.apply_value_str_by_name(driver, "lastname", contact.lastname)
            self.app.apply_value_str_by_name(driver, "address", contact.address)
            self.app.apply_value_str_by_name(driver, "email", contact.email)
            self.app.apply_value_str_by_name(driver, "byear", contact.byear)
            self.app.apply_value_dropdown_by_name(driver,"bmonth",contact.bmonth) #dropdown
            self.app.apply_value_dropdown_by_name(driver, "bday", contact.bday) #dropdown
            self.app.apply_value_str_by_name(driver, "mobile", contact.mobile)
            self.app.apply_value_str_by_name(driver, "homepage", contact.homepage)

            self.app.apply_value_str_by_name(driver, "middlename", contact.middlename)
            self.app.apply_value_str_by_name(driver, "nickname", contact.nickname)
            self.app.apply_value_str_by_name(driver, "photo", contact.photo)
            self.app.apply_value_str_by_name(driver, "delete", contact.delete)
            self.app.apply_value_str_by_name(driver, "company", contact.company)
            self.app.apply_value_str_by_name(driver, "title", contact.title)
            self.app.apply_value_str_by_name(driver, "home", contact.home)
            self.app.apply_value_str_by_name(driver, "work", contact.work)
            self.app.apply_value_str_by_name(driver, "fax", contact.fax)
            self.app.apply_value_str_by_name(driver, "email2", contact.email2)
            self.app.apply_value_str_by_name(driver, "email3", contact.email3)
            self.app.apply_value_str_by_name(driver, "aday", contact.aday) #dropdown
            self.app.apply_value_str_by_name(driver, "amonth", contact.amonth)  # dropdown
            self.app.apply_value_str_by_name(driver, "ayear", contact.ayear)
            self.app.apply_value_str_by_name(driver, "new_group", contact.new_group)
            self.app.apply_value_str_by_name(driver, "address2", contact.address2)
            self.app.apply_value_str_by_name(driver, "phone2", contact.phone2)
            self.app.apply_value_str_by_name(driver, "notes", contact.notes)

        with allure.step("Submit contact creation"):
            driver.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()

    def edit_first_contact(self,contact):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step("Select a contact"):
            driver.find_element(By.NAME, "selected[]").click()

        with allure.step("Edit contact"):
            driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
            self.app.apply_value_str_by_name(driver, "firstname", contact.firstname,True)
            self.app.apply_value_str_by_name(driver, "lastname", contact.lastname,True)
            self.app.apply_value_str_by_name(driver, "address", contact.address,True)
            self.app.apply_value_str_by_name(driver, "email", contact.email,True)
            self.app.apply_value_str_by_name(driver, "byear", contact.byear,True)
            self.app.apply_value_dropdown_by_name(driver, "bmonth", contact.bmonth)  # dropdown
            self.app.apply_value_dropdown_by_name(driver, "bday", contact.bday)  # dropdown
            self.app.apply_value_str_by_name(driver, "mobile", contact.mobile,True)
            self.app.apply_value_str_by_name(driver, "homepage", contact.homepage,True)

            self.app.apply_value_str_by_name(driver, "middlename", contact.middlename,True)
            self.app.apply_value_str_by_name(driver, "nickname", contact.nickname,True)
            self.app.apply_value_str_by_name(driver, "photo", contact.photo,True)
            self.app.apply_value_str_by_name(driver, "delete", contact.delete,True)
            self.app.apply_value_str_by_name(driver, "company", contact.company,True)
            self.app.apply_value_str_by_name(driver, "title", contact.title,True)
            self.app.apply_value_str_by_name(driver, "home", contact.home,True)
            self.app.apply_value_str_by_name(driver, "work", contact.work,True)
            self.app.apply_value_str_by_name(driver, "fax", contact.fax,True)
            self.app.apply_value_str_by_name(driver, "email2", contact.email2,True)
            self.app.apply_value_str_by_name(driver, "email3", contact.email3,True)
            self.app.apply_value_str_by_name(driver, "aday", contact.aday)  # dropdown
            self.app.apply_value_str_by_name(driver, "amonth", contact.amonth)  # dropdown
            self.app.apply_value_str_by_name(driver, "ayear", contact.ayear,True)
            self.app.apply_value_str_by_name(driver, "new_group", contact.new_group,True)
            self.app.apply_value_str_by_name(driver, "address2", contact.address2,True)
            self.app.apply_value_str_by_name(driver, "phone2", contact.phone2,True)
            self.app.apply_value_str_by_name(driver, "notes", contact.notes,True)


        with allure.step("Update contact"):
            driver.find_element(By.NAME, "update").click()

    def delete_first_contact(self):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step("Select a contact"):
            driver.find_element(By.NAME, "selected[]").click()
        with allure.step("Delete a contact"):
            driver.find_element(By.XPATH,"//input[@value='Delete']").click()