import allure
from model.contact import Contact


@allure.epic("Check_contact_fields home page")
@allure.description("This test check contact fields home page")

def test_check_contacts_filds_home_page(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact_fields", home="+356-67-78", email="email@test.com"))
    contact_from_bd = sorted(orm.get_contact_list(),key=Contact.id_or_max)
    contact_from_home_page = sorted(app.contact.get_contact_list(),key=Contact.id_or_max)
    assert app.contact.compare_contacts(contact_from_bd, contact_from_home_page)



