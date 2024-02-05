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
    group = Group(name, header, footer)
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
