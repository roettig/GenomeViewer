# verwaltet Farbe, Schriftgroesse, Style, usw. der Sequenz, der Nummerierung und der Features
# bis jetzt nur ansatzweise

import wx
import wx.richtext as rt
from Observable import Observable

class Layout(Observable):
    seqSize=0
    numSize=0
    bgColor=wx.Color(255, 255, 255) #white
    seqColor=wx.Color(0,0,0) #black
    numColor=wx.Color(0,0,0) #black
    colorList=[]
    #Listen-Iterator, der ueber die Farbliste iteriert
    colListIter=iter(colorList)
    typeColDict={}
    leftIndent=0
    lineSpacing=0
    def __init__(self, initial_seqSize=10, initial_numSize=8, initial_bgColor=wx.Color(255, 255, 255), initial_seqColor=wx.Color(0,0,0), initial_numColor=wx.Color(0,0,0), initial_leftIndent=50, initial_lineSpacing=20):
        self.seqSize=initial_seqSize
        self.numSize=initial_numSize
        self.bgColor=initial_bgColor
        self.seqColor=initial_seqColor
        self.numColor=initial_numColor
        self.colorList=initial_colorList=['#00FF00', '#0000FF', '#FF0000', '#008000', '#808080' '#FF00FF', '#00FFFF', '#800000', '#808000', '#000080', '#800080', '#008080', '#C0C0C0', '#A52A2A', '#7FFF00']
        self.colListIter=iter(self.colorList)
        self.leftIndent=initial_leftIndent
        self.lineSpacing=initial_lineSpacing
        #wxx=wx.App()
        #self.seqFont=wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD)
        #self.numFont=wx.Font(8, wx.MODERN, wx.NORMAL, wx.BOLD)
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
    def setBgColor(self, color):
        self.bgColor=color
        self.setChanged()
    def getBgColor(self):
        return self.bgColor
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
    def getSeqFont(self):
        return wx.Font(self.seqSize, wx.MODERN, wx.NORMAL, wx.BOLD)
        #return self.seqFont
    def setSeqFont(self, font):
        self.seqFont = font
        self.setChanged()
    def getNumFont(self):
        return wx.Font(self.numSize, wx.MODERN, wx.NORMAL, wx.BOLD)
        #return self.numFont
    def setNumFont(self, font):
        self.numFont=font
        self.setChanged()
    def getSeqTextAttrEx(self):
        rta = rt.RichTextAttr()
        rta.SetFont(self.getSeqFont())
        rta.SetTextColour(self.seqColor)
        rta.SetBackgroundColour(self.bgColor)
        # leftindent und linespacing wird nicht angezeigt
        rta.SetLeftIndent(self.leftIndent)
        return rta
    def getNumTextAttrEx(self):
        rta = rt.RichTextAttr()
        rta.SetFont(self.getNumFont())
        rta.SetTextColour(self.numColor)
        rta.SetBackgroundColour(self.bgColor)
        rta.SetLineSpacing(self.lineSpacing)
        return rta
    # weist einem Typ eine Farbe zu, falls dieser noch nicht im Dictionary vorhanden
    def addTypeColDict(self, type):
        if not self.typeColDict.has_key(type):
            self.typeColDict[type]=self.colListIter.next()
            print self.typeColDict
    def getTypeColDict(self, key):
        return self.typeColDict.get(key)