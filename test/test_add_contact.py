import pytest
from model.conact import Contact
import allure
from fixture.application import Application


@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture

@allure.epic("Contact")
class TestAddContact():
  data_test = [
    ("Firstname203", "Lastname", "Minsk Kalinina 18-304", "email@test.by", "+375440000000", "1994", "January","2","https://www.google.com/"),
    ("","","","","","","","-","")
  ]

  @pytest.mark.parametrize('firstname, lastname, address, email, mobile, byear, bmonth, bday, homepage', data_test)
  @allure.description("This test successfully creates a contact")
  def test_add_contact(self,app, firstname,lastname,address,email, mobile, byear, bmonth, bday, homepage):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname,lastname,address,email, mobile,byear,bmonth,bday,homepage))
    app.logout()









