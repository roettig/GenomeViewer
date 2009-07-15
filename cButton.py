import  wx.lib.colourselect as  csel
import wx

class cButton(csel.ColourSelect):
    """class to set colours of features via button"""
    #def __init__(self, type, color, size=(60, 20)):
    def __init__(self, parent, colour, type, id=wx.ID_ANY, label="", pos=wx.DefaultPosition, size=(60, 20), callback=None, style=0):
        csel.ColourSelect.__init__(self, parent, id, label, colour, pos, size, callback, style)

        self.type=type

    def getType(self):
        return self.type