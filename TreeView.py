# -*- coding: utf-8 -*-
import wx
import Imports
from IObserver import IObserver
#from Observable import Observable
from FeatureListContainer import FeatureListContainer
from Genome import Genome
from GenomeView import GenomeView
from GenomeModel import GenomeModel


class TreeView(wx.Panel, IObserver):
	""" displays search results and annotations in a treeview-widget """
	
	def __init__(self, observed, model, *args, **kwargs):
		""" initializes TreeView """
		wx.Panel.__init__(self, style=wx.BORDER_SUNKEN, *args, **kwargs)    

		self.model = model
		self.tree = wx.TreeCtrl(self, -1)
		self.root = self.tree.AddRoot("Features")
		self.searchResults = self.tree.AppendItem(self.root, "Search Results")
		self.ptt = self.tree.AppendItem(self.root, "PTT-Imports")
		self.gff = self.tree.AppendItem(self.root, "GFF-Imports")
		self.tree.Expand(self.root)

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(self.tree, 1, flag= wx.GROW | wx.EXPAND)

		self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,
			self.OnActivated,
			self.tree)
		self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnTreeRightClick, self.tree)
		self.SetSizer(hbox)
		self.Show(True)

	def AddTreeNodes(self, parentItem, items):
		""" adds nodes to TreeView (given as item-list) """
		for item in items:
		    iid = self.tree.AppendItem(parentItem, item.getType())
		    self.tree.SetPyData(iid,item)


	def GetItemText(self, item):
		""" returns text of an item """
		if item:
			return self.tree.GetItemText(item)
		else:
			return ""
	def OnTreeRightClick(self, evt):
		""" activates/inactivates right-clicked annotation """
		item = evt.GetItem()
		feature = self.tree.GetItemPyData(item)
		if feature.getActive() == True:
			feature.setActive(False)
		else:
			feature.setActive(True)
		Imports.con.setChanged()

	def OnActivated(self, evt):
		""" jumps to marked annotation in GenomeView """
		genome = Imports.genome
		item = evt.GetItem()
		feature = self.tree.GetItemPyData(item)

		#setzt neue position in die mitte des features(bis jetzt nur mit hard-coded range)
		position = (feature.getStart() + feature.getEnd())/2
		startpos = max(0, position - 2500)
		endpos = min(genome.getSequenceLength(), position + 2500)

		#aktualisiert textview
		self.model.setRanges(startpos, endpos)
		self.model.setPosition(position)


	def update(self, source, object):
		""" observer update method """
		self.tree.DeleteAllItems()
		self.root = self.tree.AddRoot("Features")
		self.searchResults = self.tree.AppendItem(self.root, "Search Results")
		self.ptt = self.tree.AppendItem(self.root, "PTT-Imports")
		self.gff = self.tree.AppendItem(self.root, "GFF-Imports")
		self.AddTreeNodes(self.gff, Imports.con.getGFFList())
		self.AddTreeNodes(self.ptt, Imports.con.getPTTList())
		self.tree.Expand(self.root)

