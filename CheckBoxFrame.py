import wx

class CheckBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self , None,-1,"Selection View", size = (300, 200))
        panel = wx.Panel(self,-1)
        chkbox1 = wx.CheckBox(panel, -1, "CDS", (20,10),(175,30))
        chkbox2 = wx.CheckBox(panel, -1, "Gene", (20,30),(175,30))
        chkbox3 = wx.CheckBox(panel, -1, "repeat region", (20,50),(175,30))
        chkbox4 = wx.CheckBox(panel, -1, "Zusatz", (20,70),(175,30))
        btn1 = wx.Button(panel, -1, "color features", (150,100), (90,20))
        chkbox1.Show()
        chkbox2.Show()
        chkbox3.Show()
        chkbox4.Show()
        btn1.Show()
        self.Show()

        def CheckCheckboxes(self):
            pass


        def OnExit(self):
            self.Close()


if __name__ == "__main__":
    app = wx.PySimpleApp()
    CheckBoxFrame().Show()
    app.MainLoop()
