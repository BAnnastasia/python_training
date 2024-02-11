import pytest
from model.contact import Contact
import allure
from fixture.application import Application

@allure.epic("Contact_create")
class TestAddContact():
  data_test = [
    ("Firstname111", "Lastname11", "Minsk Kalinina 18-304", "+375440000000y", "email1@test.by", "1994", "January","-","https://www.google.com/",
     None, None, None, None, None, None,"+453435home", "+666-6767work", None, "222email@test", "test33@email.by", None, None, None, None, None,None, None),
    #(None, '', None, None, None, None, None, None, None,
     #None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,)

  ]

  @pytest.mark.parametrize('firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage, middlename, nickname, photo, delete, company, title, home, work, fax, email2, email3, aday, amonth, ayear,new_group, address2, phone2, notes', data_test)
  @allure.description("This test successfully creates a contact")
  def test_add_contact(self,app, firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage,
                 middlename, nickname, photo, delete,
                 company, title,
                 home, work, fax,
                 email2, email3,
                 aday, amonth, ayear,
                 new_group, address2, phone2, notes):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname, lastname, address, mobile, email, byear, bmonth, bday, homepage,
                 middlename, nickname, photo, delete,
                 company, title,
                 home, work, fax,
                 email2, email3,
                 aday, amonth, ayear,
                 new_group, address2, phone2, notes)
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)









