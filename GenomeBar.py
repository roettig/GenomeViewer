# -*- coding: utf-8 -*-

import wx
import Imports
from Observable import Observable
from GenomeModel import GenomeModel


        #barImg = wx.Image('GenomeBar.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        #wx.StaticBitmap(self, -1, barImg, (10, 10), (barImg.GetWidth(), barImg.GetHeight()))
        #!/usr/bin/python

#RW = Imports.genome.getSequenceLength() # ruler widht
#RM = 10  # ruler margin
#RH = 60  # ruler height

class GenomeBar(wx.Panel, Observable):
    
    def __init__(self, model, *args, **kwargs):
       
        #super(GenomeView,self).__init__(*args, **kwargs)
        wx.Panel.__init__(self, style=wx.BORDER_SUNKEN, *args, **kwargs)
        self.font = wx.Font(7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD, False, 'Courier 10 Pitch')
        
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

        self.model = model
        self.Centre()
        self.Show(True)

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
        
        dc = wx.PaintDC(self)
        width, heigth = self.GetSize()
        margin = 10

        #brush = wx.BrushFromBitmap(wx.Bitmap('GenomeBar.jpg'))
        #dc.SetBrush(brush)
        dc.SetPen(wx.Pen('#FFFFFF', 1, wx.TRANSPARENT))
        dc.DrawRectangle(0, 0, width, heigth)
        dc.SetFont(self.font)

        dc.SetPen(wx.Pen('#000000'))
#       dc.SetTextForeground('#000000')
#
#        for i in range(width):
#            if not (i % 100):
#                dc.DrawLine(i+margin, 0, i+margin, 10)
#                w, h = dc.GetTextExtent(str(i))
#                dc.DrawText(str(i), i+margin-w/2, 11)
#            elif not (i % 20):
#                dc.DrawLine(i+margin, 0, i+margin, 8)
#            elif not (i % 2): dc.DrawLine(i+margin, 0, i+margin, 4)
        
        pos = self.genomePosToMousePos(self.model.getPosition())
        dc.DrawLine(pos, 0, pos, heigth)

        