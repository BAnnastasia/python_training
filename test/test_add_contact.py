from model.contact import Contact
import allure


@allure.epic("Contact_create")
@allure.description("This test successfully creates a contact")
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contact = db.get_contact_list()
    app.contact.create(contact)
    new_contact = db.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        new_contact2 = app.contact.get_contact_list()
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(new_contact2, key=Contact.id_or_max)