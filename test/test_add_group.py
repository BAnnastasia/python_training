import pytest
import allure
from model.group import Group


@allure.epic("Group_create")
class TestAddGroup():
  data_test = [
      ("Name_group","header_group","footer_group"),
      ("","",""),
      #("Friends ", "list", "best"),
      #("Test", None, None)
  ]


  @pytest.mark.parametrize('name,header,footer', data_test)
  @allure.description("This test successfully creates a group")
  def test_add_group(self, app, name, header, footer):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name, header, footer))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)