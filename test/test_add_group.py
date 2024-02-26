import allure
from model.group import Group

@allure.epic("Group_create")
@allure.description("This test successfully creates a group")
def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list() #app.group.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list() #app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
