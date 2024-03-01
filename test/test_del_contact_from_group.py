import allure
from model.contact import Contact
from model.group import Group
import random

@allure.epic("Delete contact from group")
def test_del_from_group(app, orm):
    contact = Contact(firstname="Test_del_contact_to_group")
    app.contact.create(contact)
    if (len(orm.get_group_list()) == 0):
        app.group.create(Group(name="test_group"))
    contact_new = sorted(orm.get_contact_list(), key=Contact.id_or_max)[-1]
    list_group = orm.get_group_list()
    group_random = random.choice(list_group)
    app.contact.add_to_group_by_id(contact_new.id, group_random.id)
    list_contact = orm.get_contacts_in_group(group_random)
    assert contact_new in list_contact
    app.contact.delete_contact_from_group_by_id(contact_new.id, group_random.id)
    list_contact_not=orm.get_contacts_not_in_group(group_random)
    assert contact_new in list_contact_not