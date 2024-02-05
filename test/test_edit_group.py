import allure
import pytest
from model.group import Group

data_test = [
    ("Edit_name","edit_header", None),
    #("","","")

  ]
@allure.epic("Group_edit")
@allure.description("This test successfully edit a group")
@pytest.mark.parametrize('name,header,footer,', data_test)
def test_edit_first_group(app, name, header, footer):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name2", footer="footer4"))
    old_groups = app.group.get_group_list()
    group = Group(name, header, footer)
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)