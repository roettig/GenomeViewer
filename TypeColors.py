import wx
import  wx.lib.scrolledpanel as scrolled
import  wx.lib.colourselect as  csel
from cButton import cButton
from Observable import Observable

class TypeColors(wx.Frame, Observable):

    """contains informations about every color of each type of sequence"""

    dictionary={}
    def __init__(self, parent, dictionary):
        self.dictionary=dictionary
        types = self.dictionary.keys()
        colors= self.dictionary.values()

        if len(types) != 0:

            wx.Frame.__init__(self , None,-1,"Change Type Colors")

            fgSizer=wx.FlexGridSizer(cols=2, vgap=5, hgap=4)
            hSizer=wx.BoxSizer(wx.HORIZONTAL)

            panel1=scrolled.ScrolledPanel(self, -1, size=(400,300), style=wx.SUNKEN_BORDER)
            panel2=wx.Panel(self, -1)

            t=wx.StaticText(panel1, -1, 'Types')
            c=wx.StaticText(panel1, -1, 'Colors')
            font=wx.Font(10, wx.NORMAL, wx.NORMAL, wx.BOLD)
            t.SetFont(font)
            c.SetFont(font)

            fgSizer.AddMany([(t), (c)])



            for type in types:
                label=wx.StaticText(panel1, -1, type)
                color=self.dictionary.get(type)
                button = cButton(panel1, color, type)
                button.Bind(csel.EVT_COLOURSELECT, self.OnSelectColour)

                fgSizer.Add(label)
                fgSizer.Add(button)


            hSizerPanel1=wx.BoxSizer(wx.HORIZONTAL)
            hSizerPanel1.Add(fgSizer, 0, wx.TOP|wx.LEFT, 10)
            panel1.SetSizer(hSizerPanel1)
            panel1.SetAutoLayout(1)
            panel1.SetupScrolling()

            #Buttons
            okButton=wx.Button(panel2, -1, "OK")
            self.Bind(wx.EVT_BUTTON, self.OnOkButton, id=okButton.GetId())
            cancelButton=wx.Button(panel2, -1, "Cancel")
            self.Bind(wx.EVT_BUTTON, self.OnCancelButton, id=cancelButton.GetId())

            hSizer.Add(okButton, 1, wx.ALL|wx.EXPAND)
            hSizer.Add(cancelButton, 1, wx.ALL|wx.EXPAND)
            panel2.SetSizer(hSizer)
            panel2.SetAutoLayout(1)



            vsizer = wx.BoxSizer(wx.VERTICAL)
            vsizer.Add(panel1, 1, wx.EXPAND)
            vsizer.Add(panel2, 0, wx.EXPAND)

            self.SetSizer(vsizer)
            self.SetAutoLayout(1)

            self.SetMaxSize(self.GetSize())
            self.SetMinSize(self.GetSize())

            self.SetAutoLayout(1)
            self.Show()

        else:
            dlg = wx.MessageDialog(parent, "No Annotations loaded")
            dlg.ShowModal()
            dlg.Destroy()

    def OnApplyButton(self, evt):
        self.setChanged()
    def OnOkButton(self, evt):
        self.setChanged()
        self.Close()
    def OnCancelButton(self, evt):
        self.Close()

    def OnExit(self):
        self.Close()

    def OnSelectColour(self, evt):
        newcolor=evt.GetValue()
        obj=evt.GetEventObject()
        type=obj.getType()
        self.dictionary[type]=newcolor