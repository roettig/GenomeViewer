# -*- coding: utf-8 -*-

import wx
import Imports
from IObserver import IObserver
from GenomeModel import GenomeModel


class GenomeBar(wx.Panel, IObserver):

    def __init__(self, model, *args, **kwargs):
        wx.Panel.__init__(self, style=wx.BORDER_SUNKEN, *args, **kwargs)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.width, self.height = self.GetSize()
        
        #background image
        self.barImg = wx.Image("genomebar.jpg", type=wx.BITMAP_TYPE_ANY, index=-1)
        #self.barImg.Scale(self.width, self.height)
        self.barBmp = self.barImg.ConvertToBitmap()

        #pointer image
        self.pointerImg = wx.Image("genomepointer.png", type=wx.BITMAP_TYPE_ANY, index=-1)
        self.pointerBmp = self.pointerImg.ConvertToBitmap()
        
        #cross-hair cursor
        self.cursor = wx.StockCursor(wx.CURSOR_CROSS)
        self.SetCursor(self. cursor)
        
        self.model = model
        self.Centre()
        self.Show(True)
        self.drawBar()


    def OnPaint(self, event):
        self.drawBar()


    def OnLeftDown(self, event):
        pos = event.GetPosition()
        genomePos = self.mousePosToGenomePos(pos[0])
        #print "#",genomePos
        startpos = max(0, genomePos - 2500)
        endpos = min(Imports.genome.getSequenceLength(), genomePos + 2500)

        self.model.setRanges(startpos, endpos)
        self.model.setPosition(genomePos)

        self.drawBar()


    def mousePosToGenomePos(self, mPos):
        mPos = float(mPos)
        width = float(self.GetSize()[0])
        proportion = mPos / width
        genomeLength = Imports.genome.getSequenceLength()
        return int(genomeLength * proportion)


    def genomePosToMousePos(self, gPos):
        gPos = float(gPos)
        width = float(Imports.genome.getSequenceLength())
        proportion = 0
        if (width > 0):
            proportion = gPos / width
        barLength = self.GetSize()[0]
        return int(barLength * proportion)


    def drawBar(self):
        dc = wx.ClientDC(self)
        self.width, self.height = self.GetSize()  
        
        #draw background
        #self.barImg = self.barImg.Scale(self.width, self.height)
        #self.barBmp = self.barImg.ConvertToBitmap()
        #barBrush = wx.BrushFromBitmap(self.barBmp)
        dc.SetPen(wx.Pen('white', 1, wx.TRANSPARENT))
        #dc.SetBrush(barBrush)
        dc.DrawRectangle(0, 0, self.width-3.5, self.height-3.5)

        #draw pointer
        pos = self.genomePosToMousePos(self.model.getPosition())
        pos = pos - self.pointerImg.GetWidth()/2 +1
        dc.DrawBitmap(self.pointerBmp, pos, 0)


    def update(self, source, object):
        self.drawBar()
        
        
        
