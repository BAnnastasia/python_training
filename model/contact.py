from sys import maxsize


def get_or_else(value, default_value):
    return default_value if value is None else value


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, mobile=None, email=None, byear=None, bmonth=None, bday=None, homepage=None,
                 middlename=None,
                 nickname=None, photo=None, delete=None,
                 company=None, title=None,
                 home=None,
                 work=None, fax=None,
                 email2=None, email3=None,
                 aday=None, amonth=None, ayear=None,
                 new_group=None, address2=None, phone2=None, notes=None, id=None, text=None, allphones=None, allemails=None
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.mobile = mobile
        self.email = email
        self.byear = byear
        self.bmonth = bmonth #dropdown
        self.bday = bday #dropdown
        self.homepage = homepage
        self.middlename = middlename

        self.nickname = nickname
        self.photo = photo
        self.delete = delete
        self.company = company
        self.title = title
        self.home = home
        self.work = work
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.aday = aday #dropdown
        self.amonth = amonth #dropdown
        self.ayear = ayear
        self.new_group = new_group #dropdown
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones = allphones
        self.all_emails = allemails


    def __repr__(self):
        return ("Contact ID:""%s" % (self.id) + " " + "firstname:""%s" % (self.firstname) +
                " " + "lastname:""%s" % (self.lastname)+" " + "Hphone:""%s" % (self.home)+" " + "email:""%s" % (self.email))

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id)
                and get_or_else(self.firstname, '') == get_or_else(other.firstname, '')
                and get_or_else(self.lastname, '') == get_or_else(other.lastname, ''))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

