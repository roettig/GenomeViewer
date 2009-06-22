import wx

class CheckBoxFrame(object):
    def __init__(self):
        wx.Frame.__init__(self , None,-1,"Selection View", size = (200,150))
        panel = wx.Panel(self,-1)
        wx.CheckBox(panel, -1, "CDS", (50,55),(175,30))
        wx.CheckBox(panel, -1, "Gene", (60,55),(175,30))
        wx.CheckBox(panel, -1, "repeat region", (70,55),(175,30))
        wx.CheckBox(panel, -1, "Zusatz", (80,55),(175,30))




if __name__ == "__main__":
    app = wx.PySimpleApp()
    CheckBoxFrame().Show()
    app.MainLoop()
