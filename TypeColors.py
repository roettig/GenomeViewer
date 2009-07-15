import wx
import  wx.lib.scrolledpanel as scrolled
import  wx.lib.colourselect as  csel
from cButton import cButton
from Observable import Observable

class TypeColors(wx.Frame, Observable):
    dictionary={}
    def __init__(self, dictionary):

        self.dictionary=dictionary

        wx.Frame.__init__(self , None,-1,"Change Type Colors", size=(400, 400))
        sizer = wx.FlexGridSizer(cols=2, vgap=5, hgap=4)

        types = self.dictionary.keys()
        colors= self.dictionary.values()
        #print self.dictionary

        if len(types) != 0:
            self.SetMaxSize((400, 400))
            panel = scrolled.ScrolledPanel(self, -1)

            font=wx.Font(10, wx.NORMAL, wx.NORMAL, wx.BOLD)
            t=wx.StaticText(panel, -1, 'Types')
            t.SetFont(font)
            c=wx.StaticText(panel, -1, 'Colors')
            c.SetFont(font)
            sizer.AddMany([(t), (c)])
            for type in types:
                label=wx.StaticText(panel, -1, type)
                color=self.dictionary.get(type)
                #print color
                button = cButton(panel, color, type)
                button.Bind(csel.EVT_COLOURSELECT, self.OnSelectColour)

                sizer.AddMany([(label), (button)])

            #Buttons
            okButton=wx.Button(panel, -1, "OK")
            self.Bind(wx.EVT_BUTTON, self.OnOkButton, id=okButton.GetId())
            cancelButton=wx.Button(panel, -1, "Cancel")
            self.Bind(wx.EVT_BUTTON, self.OnCancelButton, id=cancelButton.GetId())

            sizer.Add(okButton)
            sizer.Add(cancelButton)
            vsizer = wx.BoxSizer(wx.VERTICAL)
            hsizer = wx.BoxSizer(wx.HORIZONTAL)
            vsizer.Add(sizer, 1, wx.GROW|wx.EXPAND|wx.ALL, 5)
            hsizer.Add(vsizer, 1, wx.GROW|wx.EXPAND)
            panel.SetSizer(hsizer)
            #panel.SetAutoLayout(1)
            panel.SetupScrolling()
            #panel.Fit()
            #self.SetAutoLayout(1)
            #self.Fit()
            #self.SetSize(panel.GetSize())
            self.SetMaxSize(self.GetSize())
            self.SetMinSize(self.GetSize())
        else:
            panel=wx.Panel(self,-1)
            label=wx.StaticText(panel, -1, 'No Annotations loaded')
            empty=wx.StaticText(panel, -1, '')
            sizer.AddMany([(label), (empty)])

            #Buttons
            okButton=wx.Button(panel, -1, "OK")
            self.Bind(wx.EVT_BUTTON, self.OnOkButton, id=okButton.GetId())
            cancelButton=wx.Button(panel, -1, "Cancel")
            self.Bind(wx.EVT_BUTTON, self.OnCancelButton, id=cancelButton.GetId())

            sizer.Add(okButton)
            sizer.Add(cancelButton)
            vsizer = wx.BoxSizer(wx.VERTICAL)
            hsizer = wx.BoxSizer(wx.HORIZONTAL)
            vsizer.Add(sizer, 1, wx.GROW|wx.EXPAND|wx.ALL, 5)
            hsizer.Add(vsizer, 1, wx.GROW|wx.EXPAND)
            panel.SetSizer(hsizer)
            panel.SetAutoLayout(1)
            panel.Fit()
            self.SetAutoLayout(1)
            self.Fit()
            self.SetMaxSize(self.GetSize())
            self.SetMinSize(self.GetSize())

        self.Centre()
        self.Show()

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
        #print self.dictionary
        #print obj.getType()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    TypeColors().Show()
    app.MainLoop()