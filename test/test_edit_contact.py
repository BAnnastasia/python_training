import allure
import pytest
from model.contact import Contact
import random


data_test = [
    ("Firstname_Edit", "Lastname_edit", "EMinsk Kalinina 18-304","+375990000000","Eemail@test.by",  "1990", "May", "13",
     "https://www.google.com/",
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
     ),

  ]

@allure.epic("Contact_edit")
@allure.description("This test successfully edit a contact")
@pytest.mark.parametrize('firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage, middlename, nickname, photo, delete, company, title, home, work, fax, email2, email3, aday, amonth, ayear,new_group, address2, phone2, notes', data_test)
def test_edit_contact(app, db, check_ui, firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage,
                 middlename, nickname, photo, delete,
                 company, title,
                 home, work, fax,
                 email2, email3,
                 aday, amonth, ayear,
                 new_group, address2, phone2, notes):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test_delete"))
    old_contact = db.get_contact_list()
    contact_random = random.choice(old_contact)
    contact = Contact(firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage,
                 middlename, nickname, photo, delete,
                 company, title,
                 home, work, fax,
                 email2, email3,
                 aday, amonth, ayear,
                 new_group, address2, phone2, notes)
    contact.id = contact_random.id

    app.contact.edit_contact_by_id(contact_random.id, contact)

    new_groups = db.get_contact_list()
    assert len(old_contact) == len(new_groups)
    new_contact = app.contact.get_contact_list()
    edited_index = next(iter([i for i in range(len(old_contact)) if old_contact[i].id == contact_random.id]))
    old_contact[edited_index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

