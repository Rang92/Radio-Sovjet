class CountryElement(object):
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.senderType = 0
        self.prev = set()
        self.inTree = False

class Tree(object):
    def __init__(self, parent = None, this = None, next = None):
        self.parent = parent
        self.this = this
        self.next = next
