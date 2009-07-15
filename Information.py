# Information.py
# Gibt die Informationen zu einem eingefaerbten Feature
import wx
import wx.richtext as rt


#class MessageDialog(wx.Frame):
#    def __init__(self, parent, id, title):
#        wx.Frame.__init__(self, parent, id, title)
#
#        wx.FutureCall(1000, self.ShowMessage)
#
#        self.Centre()
#        self.Show(True)
#
#    def ShowMessage(self):
#        test = "DESCRIPTION;DESC;DEE;D;1200;1500;TYPE"
#        info = Information(None, -1, test, 'Information')
#        info.ShowModal()
#        info.Destroy()

class Information(wx.Dialog):
    """class to get pop up information in text view"""
    def __init__(self, parent, id, string, title):
        wx.Dialog.__init__(self, parent, id, title, size=(400, 440))

        a=[]
        a = string.split(';')

        t = a.pop()
        e = a.pop()
        s = a.pop()
        d = a.pop()+'\n'
        a.reverse()

        for i in range(0,len(a)):
            d=d+a[i]+'\n'

        content =   "Start Seq Number:\t\t"+ s +'\n'+"End Seq Number:\t\t"+ e +'\n'+"LENGTH: \t\t\t"+str(int(e)-int(s))+' bp\n'+'\n'+"Description:"+'\n'+d

        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)

        typefont = wx.Font(12, wx.MODERN, wx.ITALIC, wx.NORMAL)
        numberfont = wx.Font(9, wx.MODERN, wx.ITALIC, wx.NORMAL)

        type      = wx.StaticText(panel, -1, t, (5,10))
        start     = wx.StaticText(panel, -1, "START: \t"+s, (5,35))
        end       = wx.StaticText(panel, -1, "END: \t"+e, (5,50))

        type.SetFont(typefont)
        start.SetFont(numberfont)
        end.SetFont(numberfont)

        wx.StaticText(panel, -1, 'Information:', (5, 80), (240, 150))
        rt.RichTextCtrl(panel, -1, content, (5, 100), size=(390, 295), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER | wx.HSCROLL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        closeButton = wx.Button(self, -1, 'Close', size=(70, 30))
        hbox.Add(closeButton, 1, wx.LEFT, 5)

        self.Bind(wx.EVT_BUTTON, self.OnClose, closeButton)

        vbox.Add(panel)
        vbox.Add(hbox, 1, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)

        self.SetSizer(vbox)

    def OnClose(self, event):
        self.Close()

#app = wx.App()
#MessageDialog(None, -1, 'MessageDialog')
#app.MainLoop()

