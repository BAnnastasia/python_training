import allure
from selenium.webdriver.common.by import By
class ContactHelper:
    def __init__(self,app):
        self.app = app
    def open_contact_page(self):
        driver = self.app.driver
        with allure.step("Open contact page"):
            driver.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contact):
        driver = self.app.driver
        self.open_contact_page()
        with allure.step("Fill contact form"):
            driver.find_element(By.NAME, "firstname").click()
            driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
            driver.find_element(By.NAME, "lastname").click()
            driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
            driver.find_element(By.NAME, "address").click()
            driver.find_element(By.NAME, "address").send_keys(contact.address)
            driver.find_element(By.NAME, "email").click()
            driver.find_element(By.NAME, "email").send_keys(contact.email)
            driver.find_element(By.NAME, "byear").click()
            driver.find_element(By.NAME, "byear").send_keys(contact.byear)
            driver.find_element(By.NAME, "bmonth").click()
            dropdown = driver.find_element(By.NAME, "bmonth")
            dropdown.find_element(By.XPATH, f"//option[. = '{contact.bmonth}']").click()
            driver.find_element(By.NAME, "bday").click()
            dropdown = driver.find_element(By.NAME, "bday")
            if contact.bday.isdigit():
                dropdown.find_element(By.XPATH, f"//option[. = '{int(contact.bday)}']").click()
            else:
                dropdown.find_element(By.XPATH, f"//option[. = '{contact.bday}']").click()
            driver.find_element(By.NAME, "mobile").click()
            driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
            driver.find_element(By.NAME, "homepage").click()
            driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        with allure.step("Submit contact creation"):
            driver.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()