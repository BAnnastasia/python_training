import random
import string
from model.contact import Contact
from datetime import datetime
import os.path
import getopt
import sys
import jsonpickle


try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)
n = 2
f = "data/contacts.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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

data_test = [Contact(None, '', None, None, None, None, None, None, None,
                         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                         None, None, )]+[
    Contact(random_string('firstname', 10), random_string('lastname', 10), random_string('address', 20),
                            random_phone(), random_email('email'), "1994", "January", "-", "https://www.google.com/",
                            None, None, None, None, None, None, random_phone(), random_phone(), None, "222email@test",
                            "test33@email.by", None, None, None, None, None, None, None)
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(data_test))