import allure
from model.contact import Contact


@allure.epic("Contact_delete")
@allure.description("This test successfully deletes a contact")
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_delete"))
    app.contact.delete_first_contact()
