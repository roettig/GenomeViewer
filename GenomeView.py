
import wx
import wx.richtext as rt
from IObserver import IObserver
from GenomeModel import GenomeModel

class GenomeView(wx.Panel, IObserver):
    """erstellt Textfelder, ruft Write-Methoden auf und ordnet Textfelder in Boxsizer an"""
    def __init__(self, model, *args, **kwargs):

        wx.Panel.__init__(self, style=wx.BORDER_SUNKEN, *args, **kwargs)
        self.model = model

        # TE_CENTER und TE_RIGHT wird nicht umgesetzt, ka wieso
        self.sequenceCtrl = rt.RichTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER)

        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer.Add(self.sequenceCtrl, 1, flag= wx.GROW | wx.EXPAND)

        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.Add(self.hsizer, 1, flag = wx.GROW|wx.EXPAND)
        self.SetSizer(self.vsizer)

    # ?? dafuer gibts doch die update-methode
    # wird von view aufgerufen, wenn genom geladen wurde
    # def write(self):
    #    self.model.writeSequence(self.sequenceCtrl)
    #    self.model.writeFeatures(self.sequenceCtrl)

    def update(self, source, object):
        # loescht Inhalt der Textfenster
        self.sequenceCtrl.Clear()
        #self.numerationCtrl.Clear()
        #self.sequenceCtrl.ScrollLines(100)
        self.model.writeSequence(self.sequenceCtrl)
        self.model.writeFeatures(self.sequenceCtrl)
        #geht zur angegebenen Position
        self.model.showPos(self.sequenceCtrl)
        #self.model.showFeature(999, 1352, self.sequenceCtrl)
        #print "GetClientSize(): ", self.sequenceCtrl.GetClientSize()
        print "GetSize(): ", self.sequenceCtrl.GetSize()
        #print "GetCharWidth(): ", self.sequenceCtrl.GetCharWidth()
        #print "GetCharHeight(): ", self.sequenceCtrl.GetCharHeight()
        #print "ConvertDialogSizeToPixels(): ", self.sequenceCtrl.ConvertDialogSizeToPixels((1,1))
        print self.model.getCharWidth()

    def getRtc(self):
        return self.sequenceCtrl