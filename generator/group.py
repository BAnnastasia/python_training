import random
import string
from model.group import Group
import os.path
import json
import getopt
import sys


try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)
n = 5
f = "data/groups.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = (string.ascii_letters+string.digits #+ string.punctuation
               + " "*4)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

data_test = [Group("","","")] + [
      Group(random_string("name", 10),
            random_string("header_group", 20),
            random_string("footer_group", 20))
      for i in range(n)
  ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    out.write(json.dumps(data_test, default=lambda x: x.__dict__ , indent=2))