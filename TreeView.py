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
	"""cointains methods to get tree-view"""

	def __init__(self, observed, model, *args, **kwargs):

		wx.Panel.__init__(self, style=wx.BORDER_SUNKEN, *args, **kwargs)

		self.model = model
		self.tree = wx.TreeCtrl(self)
		self.root = self.tree.AddRoot("Features")
		self.searchResults = self.tree.AppendItem(self.root, "Search Results")
		self.ptt = self.tree.AppendItem(self.root, "PTT-Imports")
		self.gff = self.tree.AppendItem(self.root, "GFF-Imports")

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(self.tree, 1, flag= wx.GROW | wx.EXPAND)

		self.Bind(wx.EVT_TREE_ITEM_EXPANDED,
			self.OnItemExpanded,
			self.tree)
		self.Bind(wx.EVT_TREE_ITEM_COLLAPSED,
			self.OnItemCollapsed,
			self.tree)
		self.Bind(wx.EVT_TREE_SEL_CHANGED,
			self.OnSelChanged,
			self.tree)
		self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,
			self.OnActivated,
			self.tree)
		self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnTreeRightClick, self.tree)
		self.SetSizer(hbox)
		self.tree.Expand(self.root)
		self.Show(True)

	def AddTreeNodes(self, parentItem, items):
		for item in items:
		    iid = self.tree.AppendItem(parentItem, item.getType())
		    self.tree.SetPyData(iid,item)


	def GetItemText(self, item):
		if item:
			return self.tree.GetItemText(item)
		else:
			return ""
	def OnTreeRightClick(self, evt):
		item = evt.GetItem()
		feature = self.tree.GetItemPyData(item)
		if feature.getActive() == True:
			feature.setActive(False)
		else:
			feature.setActive(True)
		Imports.con.setChanged()


	def OnItemExpanded(self, evt):
		pass

	def OnItemCollapsed(self, evt):
		pass

	def OnSelChanged(self, evt):
		pass

	def OnActivated(self, evt):
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
		self.tree.DeleteAllItems()
		self.root = self.tree.AddRoot("Features")
		self.searchResults = self.tree.AppendItem(self.root, "Search Results")
		self.ptt = self.tree.AppendItem(self.root, "PTT-Imports")
		self.gff = self.tree.AppendItem(self.root, "GFF-Imports")
		self.AddTreeNodes(self.gff, Imports.con.getGFFList())
		self.AddTreeNodes(self.ptt, Imports.con.getPTTList())
		for i in range(2, Imports.con.getContainerLength()):
			search = self.tree.AppendItem(self.searchResults, Imports.con.getFeatureList(i).getTitle())
			self.AddTreeNodes(search, Imports.con.getFeatureList(i))
		self.tree.Expand(self.root)
		self.tree.Expand(self.ptt)
		self.tree.Expand(self.gff)
		if self.searchResults != None:
			self.tree.Expand(self.searchResults)
		else:
			pass

