import wx
import  wx.lib.scrolledpanel as scrolled
import  wx.lib.colourselect as  csel
from cButton import cButton
from Observable import Observable

class TypeColors(wx.Frame, Observable):
    dictionary={}
    def __init__(self, dictionary):
        self.dictionary=dictionary

        frame=wx.Frame.__init__(self , None,-1,"Change Type Colors", size = (400, 500))
        #panel = scrolled.ScrolledPanel(self, -1, style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER|wx.EXPAND)
        sizer = wx.FlexGridSizer(cols=2, vgap=5, hgap=4)

        types = self.dictionary.keys()
        colors= self.dictionary.values()

        #print self.dictionary
        if len(types) != 0:
            for type in types:
                label=wx.StaticText(self, -1, type)
                color=self.dictionary.get(type)
                #print color
                button = cButton(self, color, type)
                button.Bind(csel.EVT_COLOURSELECT, self.OnSelectColour)

                sizer.AddMany([(label), (button)])
        else:
            label=wx.StaticText(self, -1, 'No Annotations loaded')
            sizer.Add(label)

        #Buttons
        okButton=wx.Button(self, -1, "OK")
        self.Bind(wx.EVT_BUTTON, self.OnOkButton, id=okButton.GetId())
        cancelButton=wx.Button(self, -1, "Cancel")
        self.Bind(wx.EVT_BUTTON, self.OnCancelButton, id=cancelButton.GetId())
        #applyButton=wx.Button(self, -1, "Apply")
        #self.Bind(wx.EVT_BUTTON, self.OnApplyButton, id=applyButton.GetId())

        sizer.Add(okButton)
        sizer.Add(cancelButton)
        #sizer.Add(applyButton)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.Add(sizer, 1, wx.GROW|wx.EXPAND|wx.ALL, 5)
        hsizer.Add(vsizer, 1, wx.GROW|wx.EXPAND)

        self.SetSizerAndFit(hsizer)
        self.SetAutoLayout(1)
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