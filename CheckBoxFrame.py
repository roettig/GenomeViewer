import wx
import Imports

class CheckBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self , None,-1,"Selection View", size = (300, 200))
        panel = wx.Panel(self,-1)
        checkbox1 = wx.CheckBox(panel, -1, "CDS", (20,10),(90,30))
        checkbox2 = wx.CheckBox(panel, -1, "Gene", (20,30),(90,30))
        checkbox3 = wx.CheckBox(panel, -1, "Start Codon", (20,50),(90,30))
        checkbox4 = wx.CheckBox(panel, -1, "Stop Codon", (20,70),(90,30))
        btn1 = wx.Button(panel, -1, "color features", (150,100), (90,20))
        #self.Bind(btn1, self.CheckCheckboxes, btn1)
        checkbox1.Show()
        checkbox2.Show()
        checkbox3.Show()
        btn1.Show()
        self.Centre()
        self.Show()

    def CheckCheckboxes(self):
        con = Imports.con
        gfflist = con.getGFFList()
        if checkbox1.checked():
            print "check1 true"
            for item in gfflist:
                if item.getDescription() == "CDS":
                     item.setActive(False)
        else:
            print "testpi"

        if checkbox2.checked():
            print "check1 true"
            for item in gfflist:
                if item.getDescription() == "gene":
                    item.setActive(False)
        else:
            print "testpi2"
        if checkbox3.Checked():
            print "test3 checked"
            for item in gfflist:
                if item.getDescription() == "start_codon":
                    item.setActive(False)
        else:
            print "testpi3"

        if checkbox4.Checked():
            print "check 4 true"
            for item in gfflist:
                if item.getDescription() == "stop_codon":
                    item.setActive(False)
        else:
            print "testpi4"

    def OnExit(self):
        self.Close()


if __name__ == "__main__":
    app = wx.PySimpleApp()
    CheckBoxFrame().Show()
    app.MainLoop()
