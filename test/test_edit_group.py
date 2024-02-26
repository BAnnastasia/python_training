import allure
import pytest
from model.group import Group
from random import randrange
import random

data_test = [
    ("Edit_name","edit_header", None),
    ("","","")

  ]
@allure.epic("Group_edit")
@allure.description("This test successfully edit a group")
@pytest.mark.parametrize('name,header,footer,', data_test)
def test_edit_group_dy_index(app, db, name, header, footer):
    if len(db.get_group_list()) == 0:
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

@pytest.mark.parametrize('name,header,footer,', data_test)
def test_edit_group_by_id(app, db, check_ui, name, header, footer):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_name2", footer="footer4"))
    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(name, header, footer)
    group.id = group_random.id
    app.group.edit_group_by_id(group_random.id, group)
    new_groups = db.get_group_list()
    edited_index = next(iter([i for i in range(len(old_groups)) if old_groups[i].id == group_random.id]))
    old_groups[edited_index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)