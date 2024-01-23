import allure
import pytest
from model.contact import Contact


data_test = [
    ("Firstname_Edit", "Lastname_Edit", "Minsk Kalinina 18-304_edit address", "edit_email@test.by", "+375550000000", "2000", "March","15","https://www.google.com/edit"),

  ]

@allure.epic("Contact_edit")
@allure.description("This test successfully edit a contact")
@pytest.mark.parametrize('firstname, lastname, address, email, mobile, byear, bmonth, bday, homepage', data_test)
def test_edit_contact(app,firstname,lastname,address,email, mobile, byear, bmonth, bday, homepage):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname, lastname, address, email, mobile, byear, bmonth, bday, homepage))
    app.session.logout()
