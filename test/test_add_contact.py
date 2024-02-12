import pytest
from model.contact import Contact
import allure
import string
import random
from datetime import datetime


def random_string(prefix, maxlen):
    symbols = (string.ascii_letters + string.digits  # + string.punctuation
               + " " * 4)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix):
    base_part = prefix
    symbols = (string.ascii_letters + string.digits)
    domain = "test.com"
    random_part = datetime.now().strftime("%m%d%Y%H%M%S") + random.choice(symbols)
    return f"{base_part}{random_part}@{domain}"


def random_phone():
    formats = [
        "({}{}{}) {}{}{}-{}{}{}{}",
        "{}{}{}{}{}{}{}{}{}{}",
        "({}{}{})-{}{}{}-{}{}{}{}",
    ]

    ten_numbers = [random.randint(0, 9) for _ in range(10)]
    return random.choice(formats).format(*ten_numbers)


@allure.epic("Contact_create")
class TestAddContact():
    data_test = [Contact(None, '', None, None, None, None, None, None, None,
                         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                         None, None, )
                 ] + [
                    Contact(random_string('firstname', 10), random_string('lastname', 10), random_string('address', 20),
                            random_phone(), random_email('email'), "1994", "January", "-", "https://www.google.com/",
                            None, None, None, None, None, None, random_phone(), random_phone(), None, "222email@test",
                            "test33@email.by", None, None, None, None, None, None, None),

                ]

    @pytest.mark.parametrize("contact", data_test)
    @allure.description("This test successfully creates a contact")
    def test_add_contact(self, app, contact):
        old_contact = app.contact.get_contact_list()
        app.contact.create(contact)
        assert len(old_contact) + 1 == app.contact.count()
        new_contact = app.contact.get_contact_list()
        old_contact.append(contact)
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
