class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "Group ID:""%s" %(self.id) +" "+ "name:""%s" %(self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name