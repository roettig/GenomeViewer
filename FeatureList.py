from Feature import Feature

class FeatureList():
    #title=""
    #active=True
    #flist=[]
    def __init__(self, title, initial_active=True, initial_flist=[]):
        self.title=title
        self.active=initial_active
        if(len(initial_flist)==0):
           self.flist=[]

    """ gets and sets Features in flist=[] """
    def getId(self, i):
        return self.flist[i].getId()
    def setId(self, i, s):
        self.flist[i].setId(s)
    def getStartPos(self, i):
        return self.flist[i].getStart()
    def setStartPos(self, i, n):
        self.flist[i].setStart(n)
    def getEndPos(self, i):
        return self.flist[i].getEnd()
    def setEndPos(self, i, n):
        self.flist[i].setEnd(n)
    def getDescription(self, i):
        return self.flist[i].getDescription()
    def setDescription(self, i, s):
        self.flist[i].setDescription(s)
    def getType(self, i):
        return self.flist[i].getType()
    def setType(self, i, s):
        self.flist[i].setType(s)
    def getFeatureActive(self, i):
        return self.flist[i].getActive()
    def setFeatureActive(self, i, bool):
        self.flist[i].setActive(bool)

    def addFeature(self, feature):
        id=str(len(self.flist))
        feature.setId(self.title + id)
        self.flist.append(feature)
    def getTitle(self):
        return self.title
    def setTitle(self, s):
        self.title=s
    def getFlist(self):
        return self.flist
    def getFlistActive(self):
        return self.active
    def setFlistActive(self,bool):
        self.active=bool
    def getLength(self):
        return len(self.flist)
    def __getitem__(self,idx):
        return self.flist[idx]
    def __len__(self):
        return len(self.flist)

"""Problem: wenn ich 2 Instanzen der Klasse FeatureList erzeuge und Features hinzufuege,
dann bekommen beide Instanzen die gleichen Features, egal bei welcher Instanz sie hinzugefuegt werden.
Ausserdem wird die Id bei getId() nicht ausgegeben"""
#fla=FeatureList("hallO")
#flb=FeatureList("teasd")
#feature1=Feature("protein1", "protein asdgqiuw", 0, 49)
#feature2=Feature("protein2", "asdgqidu", 270, 300)
#
#fla.addFeature(feature2)
#flb.addFeature(feature1)
#flb.addFeature(feature1)
#fla.addFeature(feature2)
#
#print fla is flb
#print fla.getLength()
#print flb.getLength()
#print fla.getTitle()
#print flb.getTitle()
#print fla.getType(1)
#print flb.getType(1)
#print fla.getId(0)