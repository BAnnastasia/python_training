import allure
from model.group import Group
import random


@allure.epic("Group_delete")
@allure.description("This test successfully deletes a group")
def test_delete_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_name2"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)