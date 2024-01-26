import allure
import pytest
from model.contact import Contact


data_test = [
    ("Firstname_Edit", "Lastname_edit", "EMinsk Kalinina 18-304", "Eemail@test.by", "+375990000000", "1990", "May", "13",
     "https://www.google.com/",
     None, None, None, None, None, None, "Title", None, None, None, None, None, None, None, None, None, None, None,),

  ]

@allure.epic("Contact_edit")
@allure.description("This test successfully edit a contact")
@pytest.mark.parametrize('firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage, middlename, nickname, photo, delete, company, title, home, work, fax, email2, email3, aday, amonth, ayear,new_group, address2, phone2, notes', data_test)
def test_edit_contact(app,firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage,
                 middlename, nickname, photo, delete,
                 company, title,
                 home, work, fax,
                 email2, email3,
                 aday, amonth, ayear,
                 new_group, address2, phone2, notes):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage,
                 middlename, nickname, photo, delete,
                 company, title,
                 home, work, fax,
                 email2, email3,
                 aday, amonth, ayear,
                 new_group, address2, phone2, notes))
    app.session.logout()