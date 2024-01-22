import pytest
import allure
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
@allure.epic("Group")
class TestAddGroup():
  data_test = [
      ("test_name11","test_header","test_footer"),
      ("","",""),
      ("Фикстура ", "тест", "test")
  ]
  @pytest.mark.parametrize('name,header,footer,', data_test)
  @allure.description("This test successfully creates a group")
  def test_add_group(self, app, name, header, footer):
    app.login(username="admin", password="secret")
    app.create_group(Group(name, header, footer))
    app.logout()

