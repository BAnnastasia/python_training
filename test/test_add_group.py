import pytest
import allure
from model.group import Group
import random
import string

def random_string(prefix, maxlen):
    symbols = (string.ascii_letters+string.digits #+ string.punctuation
               + " "*4)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


@allure.epic("Group_create")
class TestAddGroup():
  data_test = [Group("","","")] + [
      Group(random_string("name", 10),
            random_string("header_group", 20),
            random_string("footer_group", 20))
      for i in range(5)
  ]


  @pytest.mark.parametrize('group', data_test, ids=
                           [repr(x) for x in data_test])
  @allure.description("This test successfully creates a group")
  def test_add_group(self, app, group):
    old_groups = app.group.get_group_list()
    #group = Group(name, header, footer)
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
