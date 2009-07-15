# verwaltet Farbe, Schriftgroesse, Style, usw. der Sequenz, der Nummerierung und der Features
# bis jetzt nur ansatzweise

import wx
import wx.richtext as rt
import random
from Observable import Observable

class Layout(Observable):
    seqSize=0
    numSize=0
    seqColor=wx.Color(0,0,0) #black
    numColor=wx.Color(0,0,0) #black
    colorList=[]
    #Listen-Iterator, der ueber die Farbliste iteriert
    colListIter=iter(colorList)
    typeColDict={}
    leftIndent=0
    lineSpacing=0
    seqStyle=wx.NORMAL
    seqWeight=wx.BOLD
    upperCase = True
    charsPerLine=0
    def __init__(self, initial_seqSize=10, initial_numSize=8, initial_seqColor=wx.Color(0,0,0), initial_numColor=wx.Color(0,0,0), initial_leftIndent=50, initial_lineSpacing=20, initial_charsPerLine=50):
        self.seqSize=initial_seqSize
        self.numSize=initial_numSize
        self.seqColor=initial_seqColor
        self.numColor=initial_numColor
        self.colorList=initial_colorList=[wx.Color(139 ,0, 0), wx.Color(0, 0, 255), wx.Color(84, 139, 84),wx.Color(0, 0, 139)]
        self.colListIter=iter(self.colorList)
        self.typeColDict={}
        self.leftIndent=initial_leftIndent
        self.lineSpacing=initial_lineSpacing
        self.seqStyle=wx.NORMAL
        self.seqWeight=wx.BOLD
        self.upperCase = True
        self.charsPerLine=initial_charsPerLine
    def setSeqSize(self,n):
        self.seqSize=n
        self.setChanged()
    def getSeqSize(self):
        return self.seqSize
    def setNumSize(self,n):
        self.numSize=n
        self.setChanged()
    def getNumSize(self):
        return self.numSize
    def setSeqColor(self, color):
        self.seqColor=color
        self.setChanged()
    def getSeqColor(self):
        return self.seqColor
    def setNumColor(self, color):
        self.numColor=color
        self.setChanged()
    def getNumColor(self):
        return self.numColor
    def getFeatureListColor(self, i):
        return self.colorList[i]
    def getLeftIndent(self):
        return self.leftIndent
    def setLeftIndent(self, int):
        self.leftIndent=int
        self.setChanged()
    def getLineSpacing(self):
        return self.lineSpacing
    def setLineSpacing(self, int):
        self.lineSpacing=int
        self.setChanged()
    def getSeqStyle(self):
        return self.seqStyle
    def setSeqStyle(self, style):
        self.seqStyle=style
        self.setChanged()
    def getSeqWeight(self):
        return self.seqWeight
    def setSeqWeight(self, weight):
        self.seqWeight=weight
        self.setChanged()
    def getUpperCase(self):
        return self.upperCase
    def setUpperCase(self, bool):
        self.upperCase=bool
        self.setChanged()
    def getSeqFont(self):
        #return wx.Font(self.seqSize, wx.MODERN, wx.NORMAL, self.seqWeight)
        return wx.Font(self.seqSize, wx.MODERN, self.seqStyle, self.seqWeight)
    def setSeqFont(self, size, style, weight):
        self.seqSize=size
        self.seqStyle=style
        self.seqWeight=weight
        self.setChanged()
    def getNumFont(self):
        return wx.Font(self.numSize, wx.MODERN, wx.NORMAL, wx.BOLD)
    def getCharWidth(self):
        print "IsFixedWidth: ", self.getSeqFont().IsFixedWidth()
        print "IsUsingSizeInPixels: ", self.getSeqFont().IsUsingSizeInPixels()
        print "GetPixelSize: ", self.getSeqFont().GetPixelSize()
    def setNumFont(self, size):
        self.numSize=size
        self.setChanged()
    def getSeqTextAttrEx(self):
        rta = rt.RichTextAttr()
        rta.SetFont(self.getSeqFont())
        rta.SetTextColour(self.seqColor)
        # leftindent und linespacing wird nicht angezeigt
        rta.SetLeftIndent(self.leftIndent)
        return rta
    def getNumTextAttrEx(self):
        rta = rt.RichTextAttr()
        rta.SetFont(self.getNumFont())
        rta.SetTextColour(self.numColor)
        rta.SetLineSpacing(self.lineSpacing)
        return rta
    # weist einem Typ eine Farbe zu, falls dieser noch nicht im Dictionary vorhanden
    def addTypeColDict(self, type):
        if not self.typeColDict.has_key(type):
            try:
                self.typeColDict[type]=self.colListIter.next()
                #print self.typeColDict
            except StopIteration:
                r=random.randint(0, 255)
                g=random.randint(0, 255)
                b=random.randint(0, 255)
                #print r, g, b
                newcolor=wx.Color(r,g,b)
                self.typeColDict[type]=newcolor
                #print self.typeColDict
    def getTypeColDict(self, key):
        return self.typeColDict.get(key)
    def getTypeDict(self):
        return self.typeColDict
    def getCharsPerLine(self):
        return self.charsPerLine
    def setCharsPerLine(self, n):
        self.charsPerLine=n
        self.setChanged()