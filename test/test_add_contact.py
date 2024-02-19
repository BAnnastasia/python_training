import pytest
from model.contact import Contact
import allure

@allure.epic("Contact_create")
@allure.description("This test successfully creates a contact")
def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
