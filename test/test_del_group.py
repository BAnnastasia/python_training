import pytest
import allure


@allure.epic("Group_delete")
@allure.description("This test successfully deletes a group")
def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()