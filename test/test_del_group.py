import allure
from model.group import Group


@allure.epic("Group_delete")
@allure.description("This test successfully deletes a group")
def test_delete_first_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="test_name2"))
    app.group.delete_first_group()
