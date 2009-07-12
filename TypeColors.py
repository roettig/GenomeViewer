import wx
import  wx.lib.scrolledpanel as scrolled
import  wx.lib.colourselect as  csel
from cButton import cButton

class TypeColors(wx.Frame):
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
                button = cButton(type, color)
                button.Bind(csel.EVT_COLOURSELECT, self.OnSelectColour)

                sizer.AddMany([(label), (cButton)])
        else:
            label=wx.StaticText(self, -1, 'No Annotations loaded')
            sizer.Add(label)


        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.Add(sizer, 1, wx.GROW|wx.EXPAND|wx.ALL, 5)
        hsizer.Add(vsizer, 1, wx.GROW|wx.EXPAND)

        self.SetSizerAndFit(hsizer)
        self.SetAutoLayout(1)
        self.Centre()
        self.Show()

    def OnExit(self):
            self.Close()

    def OnSelectColour(self, evt):
        newcolor=evt.GetValue()
        obj=evt.GetEventObject()
        type=obj.getType()
        self.dictionary[type]=newcolor
        print self.dictionary
        print obj.GetType()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    TypeColors().Show()
    app.MainLoop()