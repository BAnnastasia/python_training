import allure


@allure.epic("Contact_delete")
@allure.description("This test successfully deletes a contact")
def test_delete_first_contact(app):
    app.contact.delete_first_contact()
