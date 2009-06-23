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

	def __init__(self, parent, id, observed, model):

		wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN, size=(400, 300))

		self.model = model
		self.tree = wx.TreeCtrl(self)
		self.root = self.tree.AddRoot("Features")
		self.searchResults = self.tree.AppendItem(self.root, "Search Results")
		self.ptt = self.tree.AppendItem(self.root, "PTT-Imports")
		self.gff = self.tree.AppendItem(self.root, "GFF-Imports")

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(self.tree, 1, flag= wx.GROW | wx.EXPAND)

		#self.treeModel = TreeModel()
		#self.treeModel.addObserver(self)

		#print model.GetImportedLabels()

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
		#self.tree.Expand(root)
		self.SetSizer(hbox)
		self.Show(True)

	def AddTreeNodes(self, parentItem, items):
		for item in items:
		    iid = self.tree.AppendItem(parentItem, item.getType())
		    self.tree.SetPyData(iid,item)
		    #print item

	def GetItemText(self, item):
		if item:
			return self.tree.GetItemText(item)
		else:
			return ""

	def OnItemExpanded(self, evt):
		pass

	def OnItemCollapsed(self, evt):
		pass

	def OnSelChanged(self, evt):
		pass

	def OnActivated(self, evt):
		genome = Imports.genome
		#model = GenomeModel()
		item = evt.GetItem()
		feature = self.tree.GetItemPyData(item)
		#print model.getStartRange()
		#print model.getEndRange()
		
		#setzt neue position in die mitte des features(bis jetzt nur mit hard-coded range)
		position = (feature.getStart() + feature.getEnd())/2
		startpos = max(0, position - 2500)
		endpos = min(genome.getSequenceLength(), position + 2500)
		
		#aktualisiert textview
		self.model.setRanges(startpos, endpos)
		print self.model.getStartRange()
		print self.model.getEndRange()
		self.model.setPosition(position)
		print "#", self.model.getPosition()
		#print model.getEndRange()
		#model.writeSequence(genome.getSequence()[startpos:endpos])

	def update(self, source, object):
		self.tree.DeleteAllItems()
		self.root = self.tree.AddRoot("Features")
		self.searchResults = self.tree.AppendItem(self.root, "Search Results")
		self.ptt = self.tree.AppendItem(self.root, "PTT-Imports")
		self.gff = self.tree.AppendItem(self.root, "GFF-Imports")
		self.AddTreeNodes(self.gff, Imports.con.getGFFList())
		self.AddTreeNodes(self.ptt, Imports.con.getPTTList())


