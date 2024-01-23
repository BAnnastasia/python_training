import allure
import pytest
from model.group import Group

data_test = [
      ("Edit_name","edit_header","")
  ]
@allure.epic("Group_edit")
@allure.description("This test successfully edit a group")
@pytest.mark.parametrize('name,header,footer,', data_test)
def test_edit_first_group(app, name, header, footer):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name, header, footer))
    app.session.logout()