import allure
import pytest
from model.contact import Contact
from random import randrange


data_test = [
    ("Firstname_Edit", "Lastname_edit", "EMinsk Kalinina 18-304", "Eemail@test.by", "+375990000000", "1990", "May", "13",
     "https://www.google.com/",
     None, None, None, None, None, None, "Title", None, None, None, None, None, None, None, None, None, None, None
     ),

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
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_delete"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage,
                 middlename, nickname, photo, delete,
                 company, title,
                 home, work, fax,
                 email2, email3,
                 aday, amonth, ayear,
                 new_group, address2, phone2, notes)
    contact.id = old_contact[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

