import allure
import pytest
from model.group import Group
from random import randrange

data_test = [
    ("Edit_name","edit_header", None),
    ("","","")

  ]
@allure.epic("Group_edit")
@allure.description("This test successfully edit a group")
@pytest.mark.parametrize('name,header,footer,', data_test)
def test_edit_first_group(app, name, header, footer):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name2", footer="footer4"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name, header, footer)
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)