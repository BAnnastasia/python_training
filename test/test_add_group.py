import pytest
import allure
from model.group import Group
from data.add_group import constant as data_test


@pytest.mark.parametrize('group', data_test, ids=[repr(x) for x in data_test])
@allure.description("This test successfully creates a group")
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    #group = Group(name, header, footer)
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
