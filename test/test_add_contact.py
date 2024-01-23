import pytest
from model.contact import Contact
import allure
from fixture.application import Application

@allure.epic("Contact_create")
class TestAddContact():
  data_test = [
    ("Firstname", "Lastname", "Minsk Kalinina 18-304", "email@test.by", "+375440000000", "1994", "January","2","https://www.google.com/"),
    ("","","","","","","","-","")
  ]

  @pytest.mark.parametrize('firstname, lastname, address, email, mobile, byear, bmonth, bday, homepage', data_test)
  @allure.description("This test successfully creates a contact")
  def test_add_contact(self,app, firstname,lastname,address,email, mobile, byear, bmonth, bday, homepage):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname, lastname, address, email, mobile, byear, bmonth, bday, homepage))
    app.session.logout()









