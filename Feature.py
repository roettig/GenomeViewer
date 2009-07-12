
class Feature(object):
    """Type of data"""
    id=""
    active=True
    type=""
    description=""
    start=0
    end=0
    def __init__(self, type, description, start, end, id="", initial_active=True):
        self.id=id
        self.active=initial_active
        self.type=type
        self.description=description
        self.start=start
        self.end=end
    def getId(self):
        return self.id
    def setId(self, s):
        self.id=id
    def getActive(self):
        return self.active
    def setActive(self, bool):
        self.active=bool
    def getType(self):
        return self.type
    def setType(self, s):
        self.type=type
    def getDescription(self):
        return self.description
    def setDescription(self, s):
        self.description=s
    def getStart(self):
        return self.start
    def setStart(self, n):
        self.start=n
    def getEnd(self):
        return self.end
    def setEnd(self, n):
        self.end=n