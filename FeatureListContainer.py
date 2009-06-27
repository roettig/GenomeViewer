from FeatureList import FeatureList
from Observable import Observable

class FeatureListContainer(Observable):
    """overall Database"""
    #featureLists=[[],[]]

    def __init__(self, initial_featureLists=[[],[]]):
        self.featureLists = []
        self.featureLists.append(FeatureList("PTT"))#initial_featureLists
        self.featureLists.append(FeatureList("GFF"))

    def addFeatureList(self, fl):
        self.featureLists.append(fl)
    def getFeatureList(self, i):
        return self.featureLists[i]
    def addFeatureToList(self, i, feature):
        self.featureLists[i].addFeature(feature)
    def getContainerLength(self):
        return len(self.featureLists)
    def addPTTList(self, pttlist):
        self.featureLists[0] = pttlist
        self.setChanged()
    def addGFFList(self, gfflist):
        self.featureLists[1] = gfflist
        self.setChanged()
        #print len(self.featureLists[1])

    """gets and sets attributes of FeatureList"""
    def getFlistActive(self, i):
        return self.featureLists[i].getFlistActive()
    def setFlistActive(self, i, bool):
        self.featureLists[i].setFlistActive(bool)
    def getFlistTitle(self, i):
        return self.featureLists[i].getTitle()
    def setFlistTitle(self, i, s):
        self.featureLists[i].setTitle(s)
    def getFlistLength(self,i):
        return self.featureLists[i].getLength()
    def getPTTList(self):
        return self.featureLists[0]
    def getGFFList(self):
        #print len(self.featureLists[1])
        return self.featureLists[1]

    """ gets and sets attributes of Features """
    def getStartPos(self, iFlist, iFeature):
        return self.featureLists[iFlist].getStartPos(iFeature)
    def setStartPos(self, iFlist, iFeature, n):
        self.featureLists[iFlist].setStartPos(iFeature, n)
    def getEndPos(self, iFlist, iFeature):
        return self.featureLists[iFlist].getEndPos(iFeature)
    def setEndPos(self, iFlist, iFeature, n):
        self.featureLists[iFlist].setEndPos(iFeature, n)
    def getDescription(self, iFlist, iFeature):
        return self.featureLists[iFlist].getDescription(iFeature)
    def setDescription(self, iFlist, iFeature, s):
        self.featureLists[iFlist].setDescription(iFeature, s)
    def getType(self, iFlist, iFeature):
        return self.featureLists[iFlist].getType(iFeature)
    def setType(self, iFlist, iFeature, s):
        self.featureLists[iFlist].setType(iFeature, s)
    def getId(self, iFlist, iFeature):
        return self.featureLists[iFlist].getId(iFeature)
    def setId(self, iFlist, iFeature, s):
        self.featureLists[iFlist].setId(iFeature, s)
    def getFeatureActive(self, iFlist, iFeature):
        return self.featureLists[iFlist].getFeatureActive(iFeature)
    def setFeatureActive(self, iFlist, iFeature, bool):
        self.featureLists[iFlist].setFeatureActive(iFeature, bool)