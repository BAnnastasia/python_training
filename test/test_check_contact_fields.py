import allure
from model.contact import Contact


@allure.epic("Check_contact_fields home page")
@allure.description("This test check contact fields home page")

def test_check_contacts_filds_home_page(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact_fields", home="+356-67-78", email="email@test.com"))
    contact_from_bd = orm.get_contact_list()
    contact_from_home_page = app.contact.get_contact_list()
    assert sorted(contact_from_bd, key=Contact.id_or_max) == sorted(contact_from_home_page, key=Contact.id_or_max)



