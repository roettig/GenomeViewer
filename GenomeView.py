# erstellt Textfelder, ruft Write-Methoden auf und ordnet Textfelder in Boxsizer an
import wx
import wx.richtext as rt
from IObserver import IObserver
from GenomeModel import GenomeModel

class GenomeView(wx.Panel, IObserver):
    def __init__(self, model, parent, id):# *args, **kwargs):
        #super(GenomeView,self).__init__(*args, **kwargs)
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN, size=(400, 300))
        self.model = model

        # TE_CENTER und TE_RIGHT wird nicht umgesetzt, ka wieso
        self.sequenceCtrl = rt.RichTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER | wx.HSCROLL)
        self.numerationCtrl = rt.RichTextCtrl(self, size=wx.Size(120, -1), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER)

        self.model.writeSequence(self.sequenceCtrl)
        self.model.writeFeatures(self.sequenceCtrl)
        self.model.writeNumeration(self.numerationCtrl, self.sequenceCtrl)

        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer.Add(self.numerationCtrl, 0, flag= wx.GROW | wx.EXPAND)
        self.hsizer.Add(self.sequenceCtrl, 1, flag= wx.GROW | wx.EXPAND)

        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.Add(self.hsizer, 1, flag = wx.GROW|wx.EXPAND)
        self.SetSizer(self.vsizer)

    def update(self, source, object):
        self.model.writeSequence(self.sequenceCtrl)
        self.model.writeFeatures(self.sequenceCtrl)
        self.model.writeNumeration(self.numerationCtrl, self.sequenceCtrl)