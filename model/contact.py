
class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, mobile=None, email=None, byear=None, bmonth=None, bday=None, homepage=None,
                 middlename=None,
                 nickname=None, photo=None, delete=None,
                 company=None, title=None,
                 home=None,
                 work=None, fax=None,
                 email2=None, email3=None,
                 aday=None, amonth=None, ayear=None,
                 new_group=None, address2=None, phone2=None, notes=None, id=None, text=None
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
        self.text = text

    def __repr__(self):
        return "Group ID:""%s" % (self.id) + " " + "name:""%s" % (self.alt)






