import pytest
import allure
from model.group import Group


@allure.epic("Group_create")
class TestAddGroup():
  data_test = [
      ("test_name11","test_header","test_footer"),
      ("","",""),
      ("test 3 ", "тест", "test")
  ]


  @pytest.mark.parametrize('name,header,footer,', data_test)
  @allure.description("This test successfully creates a group")
  def test_add_group(self, app, name, header, footer):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name, header, footer))
    app.session.logout()

