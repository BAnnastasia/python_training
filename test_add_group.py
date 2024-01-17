import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from group import Group


@allure.epic("Group")
class Test_add_group():
  data_test = [
      ("test_name11","test_header","test_footer"),
      ("","","")
  ]
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  @pytest.mark.parametrize('name,header,footer,', data_test)
  @allure.description("This test successfully creates a group")
  def test_add_group(self,name, header, footer):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_groups_page()
    self.create_group(Group(name, header, footer))
    self.return_to_groups_page()
    self.logout()

  def logout(self):
      with allure.step("Logout"):
          self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def return_to_groups_page(self):
      with allure.step("Return group page"):
          self.driver.find_element(By.LINK_TEXT, "group page").click()

  def create_group(self, group):
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

  def open_groups_page(self):
      with allure.step("Open groups page"):
          self.driver.find_element(By.LINK_TEXT, "groups").click()

  def login(self, username, password):
      with allure.step("Login"):
          self.driver.find_element(By.NAME, "user").click()
          self.driver.find_element(By.NAME, "user").send_keys(username)
          self.driver.find_element(By.NAME, "pass").click()
          self.driver.find_element(By.NAME, "pass").send_keys(password)
          self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()

  def open_home_page(self):
      with allure.step("Open home page"):
          self.driver.get("http://mac-minik.local/addressbook/index.php")
