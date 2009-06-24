# -*- coding: utf-8 -*-

import wx
from Observable import Observable
from GenomeModel import GenomeModel

class GenomeBar(wx.Panel, Observable):
    """erstellt Textfelder, ruft Write-Methoden auf und ordnet Textfelder in Boxsizer an"""
    def __init__(self, parent, id):# *args, **kwargs):
        #super(GenomeView,self).__init__(*args, **kwargs)
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)

