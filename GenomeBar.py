# -*- coding: utf-8 -*-

import wx
import Imports
from IObserver import IObserver
from GenomeModel import GenomeModel


class GenomeBar(wx.Panel, IObserver):
    """ jumps to position in genome-data by clicking """

    def __init__(self, model, *args, **kwargs):
        """ initializes GenomeBar """
        wx.Panel.__init__(self, style=wx.BORDER_SUNKEN, *args, **kwargs)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.width, self.height = self.GetSize()
        
        #background image
        self.barImg = wx.Image("genomebar.jpg", type=wx.BITMAP_TYPE_ANY, index=-1)
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
        """ redraws GenomeBar """
        self.drawBar()


    def OnLeftDown(self, event):
        """ sets pointer to relative position
            jumps to position in GenomeView """
        pos = event.GetPosition()
        genomePos = self.mousePosToGenomePos(pos[0])
        startpos = max(0, genomePos - 2500)
        endpos = min(Imports.genome.getSequenceLength(), genomePos + 2500)

        self.model.setRanges(startpos, endpos)
        self.model.setPosition(genomePos)

        self.drawBar()


    def mousePosToGenomePos(self, mPos):
        """ calculates position in genome from actual mouse position
            returns integer (position in genome) """
        mPos = float(mPos)
        width = float(self.GetSize()[0])
        proportion = mPos / width
        genomeLength = Imports.genome.getSequenceLength()
        return int(genomeLength * proportion)


    def genomePosToMousePos(self, gPos):
        """ calculates position in genome-bar from actual genome position
            returns integer (position in genome-bar) """
        gPos = float(gPos)
        width = float(Imports.genome.getSequenceLength())
        proportion = 0
        if (width > 0):
            proportion = gPos / width
        barLength = self.GetSize()[0]
        return int(barLength * proportion)


    def drawBar(self):
        """ draws GenomeBar """
        dc = wx.ClientDC(self)
        self.width, self.height = self.GetSize()  
        
        #draw background
        #self.barImg = self.barImg.Scale(self.width, self.height)
        #self.barBmp = self.barImg.ConvertToBitmap()
        #barBrush = wx.BrushFromBitmap(self.barBmp)
        #dc.SetPen(wx.Pen('white', 1, wx.TRANSPARENT))
        #dc.SetBrush(barBrush)
        dc.SetPen(wx.Pen('white'))
        dc.DrawRectangle(0, 0, self.width-3.5, self.height-3.5)
        
        #draw scale
        dc.SetPen(wx.Pen('black'))
        for i in range(self.width):
            if i != 0: #no zero on first bar
                if i != 0 | Imports.genome.getSequenceLength() != 0: #no genome no scale
                    if not (i % 100): #extra-long bar with numeration each 100 bars
                        dc.DrawLine(i, self.height/2 -10, i, self.height/2 + 13)
                        w, h = dc.GetTextExtent(str(self.mousePosToGenomePos(i))) #numeration = genome-pos
                        if (self.height/2 -30) >= 0: #no negative position on panel
                            dc.DrawText(str(self.mousePosToGenomePos(i)), i-w/2, self.height/2 -30)
                        else: dc.DrawText(str(self.mousePosToGenomePos(i)), i-w/2, 0)
                    elif not (i % 20): #longer bar each 20 bars
                        dc.DrawLine(i, self.height/2 -8, i, self.height/2 +8)
                    elif not (i % 2): dc.DrawLine(i, self.height/2 -4, i, self.height/2 +4) #all other short bars

        #draw pointer
        pos = self.genomePosToMousePos(self.model.getPosition())
        pos = pos - self.pointerImg.GetWidth()/2 +1
        dc.DrawBitmap(self.pointerBmp, pos, 0)


    def update(self, source, object):
        """ observer update-method """
        self.drawBar()
        
        
        
