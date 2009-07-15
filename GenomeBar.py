# -*- coding: utf-8 -*-

import wx
import Imports
from IObserver import IObserver
from GenomeModel import GenomeModel
from Layout import Layout

m = 10 #scale margin

class GenomeBar(wx.Panel, IObserver):
    """contains navigation bar"""
    def __init__(self, model, *args, **kwargs):
        wx.Panel.__init__(self, style=wx.BORDER_SUNKEN, *args, **kwargs)

        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.width, self.height = self.GetSize()
        #pointer image
        #self.pointerImg = wx.Image("genomepointer.png", type=wx.BITMAP_TYPE_ANY, index=-1)
        #self.pointerBmp = self.pointerImg.ConvertToBitmap()

        #cross-hair cursor
        self.cursor = wx.StockCursor(wx.CURSOR_CROSS)
        self.SetCursor(self. cursor)

        self.model = model
        self.Centre()
        self.Show(True)
        self.drawBar()


    def OnResize(self, event):
        self.drawBar()

    def OnLeftDown(self, event):
        pos = event.GetPosition()
        genomePos = self.mousePosToGenomePos(pos[0])#, self.width-(self.width % 100)-m)
        if genomePos > Imports.genome.getSequenceLength():
            genomePos = Imports.genome.getSequenceLength()
        if genomePos < 0:#self.mousePosToGenomePos(m):
            genomePos = 0#self.mousePosToGenomePos(m)
        #print "#",genomePos
        startpos = max(0, genomePos - 2500)
        endpos = min(Imports.genome.getSequenceLength(), genomePos + 2500)

        self.model.setRanges(startpos, endpos)
        self.model.setPosition(genomePos)

        self.drawBar()


    def mousePosToGenomePos(self, mPos):
        mPos = float(mPos)
        width = float(self.GetSize()[0])# -(self.width % 100)+m-1
        proportion = mPos / width
        genomeLength = Imports.genome.getSequenceLength()
        return int(genomeLength * proportion)


    def genomePosToMousePos(self, gPos):
        gPos = float(gPos)
        width = float(Imports.genome.getSequenceLength())
        proportion = 0
        if (width > 0):
            proportion = gPos / width
        barLength = self.GetSize()[0]# -(self.width % 100)
        return int(barLength * proportion)


    def drawBar(self):
        """ draws GenomeBar """
        if Imports.genome.getSequenceLength() != 0: #no genome no genomeBar
            dc = wx.ClientDC(self)
            self.width, self.height = self.GetSize()

            dc.SetPen(wx.Pen('white', wx.SOLID))
            dc.DrawRectangle(0, 0, self.width-3.5, self.height-3.5)

            #draw scale
            dc.SetPen(wx.Pen('light blue'))
            dc.SetFont(wx.Font(7, wx.MODERN, wx.NORMAL, wx.BOLD))
            scaleWidth = self.width#want long bar at the end

            for i in range(scaleWidth):
                if i % 100 == 0: #extra-long bar with numeration each 100 bars
                    dc.DrawLine(i, self.height/2 -10, i, self.height/2 + 13)
                    w, h = dc.GetTextExtent(str(self.mousePosToGenomePos(i))) #numeration = genome-pos
                    if (self.height/2 -30) >= 0: #no negative position on panel
                        dc.DrawText(str(self.mousePosToGenomePos(i)), i-w/2, self.height/2 -30)
                    else: dc.DrawText(str(self.mousePosToGenomePos(i)), i-w/2, 0)
                elif i % 20 == 0: #longer bar each 20 bars
                    dc.DrawLine(i, self.height/2 -8, i, self.height/2 +8)
                elif i % 2 == 0: dc.DrawLine(i, self.height/2 -4, i, self.height/2 +4) #all other short bars


            #draw pointer
            dc.SetPen(wx.Pen('gray'))
            pos = self.genomePosToMousePos(self.model.getPosition())
            #pos = pos - self.pointerImg.GetWidth()/2 +1
            dc.DrawLine(pos+1, self.height/2-11, pos+1, self.height/2+14)

    def update(self, source, object):
        self.drawBar()



