import wx

class ProportionalSplitter(wx.SplitterWindow):
    def __init__(self,parent, id = -1, proportion=0.66, size = wx.DefaultSize, **kwargs):
        wx.SplitterWindow.__init__(self,parent,id,wx.Point(0, 0),size, **kwargs)
        self.SetMinimumPaneSize(50) #the minimum size of a pane.
        self.proportion = proportion
        if not 0 < self.proportion < 1:
            raise ValueError, "proportion value for ProportionalSplitter must be between 0 and 1."
        self.ResetSash()
        self.Bind(wx.EVT_SIZE, self.OnReSize)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChanged, id=id)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.firstpaint = True

    def SplitHorizontally(self, win1, win2):
        if self.GetParent() is None: return False
        return wx.SplitterWindow.SplitHorizontally(self, win1, win2,
                                                   int(round(self.GetParent().GetSize().GetHeight() * self.proportion)))

    def SplitVertically(self, win1, win2):
        if self.GetParent() is None: return False
        return wx.SplitterWindow.SplitVertically(self, win1, win2,
                                                 int(round(self.GetParent().GetSize().GetWidth() * self.proportion)))

    def GetExpectedSashPosition(self):
        if self.GetSplitMode() == wx.SPLIT_HORIZONTAL:
            total = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().height)
        else:
            total = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().width)
        return int(round(total * self.proportion))

    def ResetSash(self):
        self.SetSashPosition(self.GetExpectedSashPosition())

    def OnReSize(self, event):
        self.ResetSash()
        event.Skip()

    def OnSashChanged(self, event):
        pos = float(self.GetSashPosition())
        if self.GetSplitMode() == wx.SPLIT_HORIZONTAL:
            total = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().height)
        else:
            total = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().width)
        self.proportion = pos / total
        event.Skip()

    def OnPaint(self,event):
        if self.firstpaint:
            if self.GetSashPosition() != self.GetExpectedSashPosition():
                self.ResetSash()
            self.firstpaint = False
        event.Skip()
