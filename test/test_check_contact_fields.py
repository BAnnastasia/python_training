import allure
import pytest
from model.contact import Contact
from random import randrange
import re

@allure.epic("Check_contact_fields")
@allure.description("This test check contact fields")

def test_check_contact_filds_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact_fields", home="+356-67-78", email="email@test.com"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact()
    contact.id = old_contact[index].id
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    contact_from_edit_page.all_emails = "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clean_email(x),
                   filter(lambda x: x is not None,
                          [contact_from_edit_page.email, contact_from_edit_page.email2,
                           contact_from_edit_page.email3]))))

    contact_from_edit_page.all_phones = "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clean_phone(x),
                   filter(lambda x: x is not None,
                          [contact_from_edit_page.home, contact_from_edit_page.mobile,
                           contact_from_edit_page.work]))))

    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones == contact_from_edit_page.all_phones
    assert contact_from_home_page.all_emails == contact_from_edit_page.all_emails


def clean_phone(s):
    return re.sub("[^a-zA-Z0-9+]", "", s)


def clean_email(s):
    return re.sub(r"\s", "", s)

