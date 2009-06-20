# verwaltet Farbe, Schriftgroesse, Style, usw. der Sequenz, der Nummerierung und der Features
# bis jetzt nur ansatzweise

import wx
from Observable import Observable

class Layout(Observable):
    seqSize=0
    numSize=0
    bgColor=0
    seqColor="black"
    numColor="magenta"
    colorList=[]

    def __init__(self, initial_seqSize=10, initial_numSize=8, initial_bgColor=0, initial_seqColor="black", initial_numColor="magenta", initial_colorList=["red", "cyan", "blue", "green", "yellow", "orange"]):
        self.seqSize=initial_seqSize
        self.numSize=initial_numSize
        self.bgColor=initial_bgColor
        self.seqColor=initial_seqColor
        self.numColor=initial_numColor
        self.colorList=initial_colorList
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
    def getDefaultFont(self):
        return wx.Font(self.seqSize, wx.MODERN, wx.NORMAL, wx.BOLD)