import allure
from model.contact import Contact
import random


@allure.epic("Contact_delete")
@allure.description("This test successfully deletes a contact")
def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test_delete"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    new_groups = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_groups)
    new_contact = db.get_contact_list()
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)