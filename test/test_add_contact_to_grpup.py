import allure
from model.contact import Contact
from model.group import Group
import random

@allure.epic("Add contact to group")
def test_add_group(app, orm):
    contact = Contact(firstname="Test_add_contact_to_group")
    app.contact.create(contact)
    contact_new = sorted(orm.get_contact_list(), key=Contact.id_or_max)[-1]
    print(contact_new)
    if (len(orm.get_group_list()) == 0):
        app.group.create(Group(name="test_group"))
    list_group = orm.get_group_list()
    group_random = random.choice(list_group)
    app.contact.add_to_group_by_id(contact_new.id, group_random.id)
    list_contact_group_random = orm.get_contacts_in_group(group_random)
    assert contact_new in list_contact_group_random                          # assert 1 == len(list(filter(lambda item: item.id == contact_new.id, list_contact_group_random)))
