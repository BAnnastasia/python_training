import allure
from selenium.webdriver.common.by import By
from model.contact import Contact
class ContactHelper:
    def __init__(self,app):
        self.app = app
    def open_new_contact_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/addressbook/edit.php") and len(driver.find_elements(By.NAME, "submit")) > 0):
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
            contact.allemails=Contact.get_all_emails(contact.email, contact.email2, contact.email3)
            contact.allphones = Contact.get_all_phones(contact.home, contact.mobile, contact.work)


    def create(self, contact):
        driver = self.app.driver
        self.open_new_contact_page()
        self.fild_contact_form(contact)
        with allure.step("Submit contact creation"):
            driver.find_element(By.XPATH, "(//input[@name='submit'])[2]").click()
            self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step(f"View contact {index}"):
            driver.find_elements(By.XPATH, "//img[@alt='Details']")[index].click()

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step(f"Edit contact {index}"):
            driver.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        id = driver.find_element(By.NAME,"id").get_attribute("value")
        firstname = driver.find_element(By.NAME,"firstname").get_attribute("value")
        lastname = driver.find_element(By.NAME,"lastname").get_attribute("value")
        address = driver.find_element(By.NAME,"address").get_attribute("value")

        homephone = driver.find_element(By.NAME,"home").get_attribute("value")
        mobilephone = driver.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = driver.find_element(By.NAME, "work").get_attribute("value")


        email = driver.find_element(By.NAME, "email").get_attribute("value")
        email2 = driver.find_element(By.NAME, "email2").get_attribute("value")
        email3 = driver.find_element(By.NAME, "email3").get_attribute("value")

        homepage = driver.find_element(By.NAME, "homepage").get_attribute("value")
        return Contact (id=id, firstname=firstname, lastname=lastname, address=address, home=homephone,
                        mobile=mobilephone, work=workphone, email=email, email2=email2, email3=email3,
                        homepage=homepage)


    def edit_contact_by_id(self, id, contact):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step(f"Edit contact {id}"):
            driver.find_element(By.XPATH,  '//a[@href="edit.php?id=%s"]' % id).click()
            self.fild_contact_form(contact, True)
        with allure.step("Update contact"):
            driver.find_element(By.NAME, "update").click()
            self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        driver = self.app.driver
        self.app.open_home_page()
        with allure.step(f"Edit contact {index}"):
            driver.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
            self.fild_contact_form(contact, True)
        with allure.step("Update contact"):
            driver.find_element(By.NAME, "update").click()
            self.contact_cache = None

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements(By.NAME,"selected[]"))

    def select_first_contact(self):
        index = 0
        with allure.step(f"Select a contact by index {index}"):
            self.select_contact_by_index(index)

    def select_contact_by_index(self, index):
        driver = self.app.driver
        with allure.step("Select a contact by index"):
             driver.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        driver = self.app.driver
        with allure.step("Select a contact by id"):
             driver.find_element(By.ID, id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_id(self, id):
        driver = self.app.driver
        self.app.open_home_page()
        self.select_contact_by_id(id)
        with allure.step("Delete a contact"):
            driver.find_element(By.XPATH,"//input[@value='Delete']").click()
            self.contact_cache = None
    contact_cache = None

    def add_to_group_by_id(self, contact_id, group_id):
        driver = self.app.driver
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        #self.app.apply_value_str_by_name(driver, "to_group", group_name)
        dropdown = driver.find_element(By.NAME, "to_group")
        dropdown.click()
        dropdown.find_element(By.CSS_SELECTOR, "option[value='%s']" % group_id).click()
        driver.find_element(By.NAME, "add").click()
        self.app.open_home_page()

    def delete_contact_from_group_by_id(self, contact_id, group_id):
        driver = self.app.driver
        self.app.open_home_page()
        dropdown = driver.find_element(By.NAME, "group")
        dropdown.click()
        dropdown.find_element(By.CSS_SELECTOR, "option[value='%s']" % group_id).click()
        self.select_contact_by_id(contact_id)
        driver.find_element(By.NAME, "remove").click()

    def compare_contacts(self, contact1, contact2):
         for item in range(len(contact1)):
            if (contact1[item].id == contact2[item].id
                    and contact1[item].firstname == contact2[item].firstname
                    and contact1[item].lastname == contact2[item].lastname
                    and contact1[item].address == contact2[item].address
                    and contact1[item].all_emails == contact2[item].all_emails
                    and contact1[item].homepage == contact2[item].homepage
                    and contact1[item].all_phones == contact2[item].all_phones):
                return True
         return False


    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        self.select_contact_by_index(index)
        with allure.step("Delete a contact"):
            driver.find_element(By.XPATH,"//input[@value='Delete']").click()
            self.contact_cache = None
    contact_cache = None
    def get_contact_list(self):
        driver = self.app.driver
        if self.contact_cache is None:
            self.app.open_home_page()
            self.contact_cache = []

            for element in driver.find_elements(By.CSS_SELECTOR,"tr[name=entry]"):

                id = element.find_elements(By.CSS_SELECTOR, "td")[0].find_element(By.TAG_NAME, "input").get_attribute("id")
                lastname = element.find_elements(By.CSS_SELECTOR, "td")[1].text
                firstname = element.find_elements(By.CSS_SELECTOR, "td")[2].text
                address = element.find_elements(By.CSS_SELECTOR, "td")[3].text
                allemails = element.find_elements(By.CSS_SELECTOR, "td")[4].text
                allphones = element.find_elements(By.CSS_SELECTOR, "td")[5].text
                homepage = element.find_elements(By.CSS_SELECTOR,"td")[9].accessible_name
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,address=address,allemails=allemails,allphones=allphones,homepage=homepage))
        return list(self.contact_cache)

