# -*- coding: utf-8 -*-
import wx
import Imports
from IObserver import IObserver
#from Observable import Observable
from FeatureListContainer import FeatureListContainer


class TreeView(wx.Panel, IObserver):
	
	def __init__(self, parent, id, observed):
	
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN, size=(400, 300))
                
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
		    print item
	
	def GetItemText(self, item):
		if item:
			return self.tree.GetItemText(item)
		else:
			return ""
	
	def OnItemExpanded(self, evt):
		print "OnItemExpanded: ", self.GetItemText(evt.GetItem())

	def OnItemCollapsed(self, evt):
		print "OnItemCollapsed: ", self.GetItemText(evt.GetItem())

	def OnSelChanged(self, evt):
		print "OnItemChanged: ", self.GetItemText(evt.GetItem())

	def OnActivated(self, evt):
		item = evt.GetItem()
		print self.tree.GetItemPyData(item)
		#print "OnActivated: ", self.GetItemText(evt.GetItem())

	def update(self, source, object):
		self.tree.DeleteAllItems()
		self.root = self.tree.AddRoot("Features")
		self.searchResults = self.tree.AppendItem(self.root, "Search Results")
		self.ptt = self.tree.AppendItem(self.root, "PTT-Imports")
		self.gff = self.tree.AppendItem(self.root, "GFF-Imports")
		print "flen=",len(Imports.con.getGFFList())
		self.AddTreeNodes(self.gff, Imports.con.getGFFList())	
		self.AddTreeNodes(self.ptt, Imports.con.getPTTList())
		#self.AddTreeNodes(self.searchResults, Imports.con.getSearchResults())
		#self.setChanged()
		
