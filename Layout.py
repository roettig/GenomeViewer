# verwaltet Farbe, Schriftgroesse, Style, usw. der Sequenz, der Nummerierung und der Features
# bis jetzt nur ansatzweise

import wx
# from Observable import Observable

class Layout:
    txtSize=0
    bgColor="white"
    txtColor="black"
    colorList=[]

    def __init__(self, initial_txtSize=10, initial_bgColor="white", initial_txtColor="black", initial_colorList=["red", "magenta", "cyan", "blue", "green", "yellow", "orange"]):
        self.txtSize=initial_txtSize
        self.bgColor=initial_bgColor
        self.txtColor=initial_txtColor
        self.colorList=initial_colorList
    def setTxtSize(self,n):
        self.txtSize=n
        # self.setChanged()
    def getTxtSize(self):
        return self.txtSize
    def setBgColor(self, color):
        self.bgColor=color
        # self.setChanged()
    def getBgColor(self):
        return self.bgColor
    def setTxtColor(self, color):
        self.TxtColor=color
        # self.setChanged()
    def getTxtColor(self):
        return self.TxtColor
    def getFeatureListColor(self, i):
        return self.colorList[i]
    def getNumerationFont(self):
        return wx.Font(self.txtSize, wx.MODERN, wx.NORMAL, wx.BOLD)
    def getSequenceFont(self):
        return wx.Font(self.txtSize, wx.MODERN, wx.NORMAL, wx.BOLD)