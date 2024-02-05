import allure
from model.contact import Contact
from random import randrange


@allure.epic("Contact_delete")
@allure.description("This test successfully deletes a contact")
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_delete"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert old_contact == new_contact