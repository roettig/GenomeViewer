import  wx.lib.colourselect as  csel
import wx

class cButton(csel.ColourSelect):
    def __init__(self, type, color, size=(60, 20)):
        # wie rufe ich den super-konstruktor auf?
        csel.ColourSelect.__init__(None, wx.ID_ANY, "", color, size)
        
        self.type=type
        self.color=color
        self.size=size
    def getType(self):
        return self.type