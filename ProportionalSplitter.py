import wx

class ProportionalSplitter(wx.SplitterWindow):
    """ realizes a splitter that can be set by proportion """
    
    def __init__(self,parent, id = -1, proportion=0.66, size = wx.DefaultSize, **kwargs):
        """ initializes a window-splitter
            that splits window in given proportion """
        wx.SplitterWindow.__init__(self,parent,id,wx.Point(0, 0),size, **kwargs)
        self.SetMinimumPaneSize(50)
        self.proportion = proportion
        if not 0 < self.proportion < 1:
            raise ValueError, "proportion value for ProportionalSplitter must be between 0 and 1."
        self.ResetSash()
        self.Bind(wx.EVT_SIZE, self.OnReSize)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChanged, id=id)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.firstpaint = True

    def SplitHorizontally(self, win1, win2):
        """ splits window horizontally
            returns wx.SplitterWindow """
        if self.GetParent() is None: return False
        return wx.SplitterWindow.SplitHorizontally(self, win1, win2,
                                                   int(round(self.GetParent().GetSize().GetHeight() * self.proportion)))

    def SplitVertically(self, win1, win2):
        """ splits window vertically
            returns wx.SplitterWindow """
        if self.GetParent() is None: return False
        return wx.SplitterWindow.SplitVertically(self, win1, win2,
                                                 int(round(self.GetParent().GetSize().GetWidth() * self.proportion)))

    def GetExpectedSashPosition(self):
        """ computes position of sash
            returns int """
        if self.GetSplitMode() == wx.SPLIT_HORIZONTAL:
            total = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().height)
        else:
            total = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().width)
        return int(round(total * self.proportion))

    def ResetSash(self):
        """ sets sash position to expected position """
        self.SetSashPosition(self.GetExpectedSashPosition())

    def OnReSize(self, event):
        """ rezizes splitted window """
        self.ResetSash()
        event.Skip()

    def OnSashChanged(self, event):
        """ actualizes sash position if changed by user """
        pos = float(self.GetSashPosition())
        if self.GetSplitMode() == wx.SPLIT_HORIZONTAL:
            total = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().height)
        else:
            total = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().width)
        self.proportion = pos / total
        event.Skip()

    def OnPaint(self,event):
        """ paint-method """
        if self.firstpaint:
            if self.GetSashPosition() != self.GetExpectedSashPosition():
                self.ResetSash()
            self.firstpaint = False
        event.Skip()
