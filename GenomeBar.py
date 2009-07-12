# -*- coding: utf-8 -*-

import wx
import Imports
from IObserver import IObserver
from GenomeModel import GenomeModel


class GenomeBar(wx.Panel, IObserver):

    def __init__(self, model, *args, **kwargs):
        wx.Panel.__init__(self, style=wx.BORDER_SUNKEN, *args, **kwargs)

        #self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

        self.model = model
        self.Centre()
        self.Show(True)
        self.drawBar()


    #def OnPaint(self, event):
        #self.drawBar()


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
        width, heigth = self.GetSize()
        dc.SetBrush(wx.Brush('#ffffff'))
        dc.SetPen(wx.Pen('#ffffff'))
        dc.DrawRectangle(0, 0, width, heigth)

        dc.SetPen(wx.Pen('#000000'))
        pos = self.genomePosToMousePos(self.model.getPosition())
        dc.DrawLine(pos, 0, pos, heigth)


    def update(self, source, object):
        self.drawBar()



