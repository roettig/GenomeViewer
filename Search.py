
import wx
import Imports
from FeatureListContainer import FeatureListContainer
from Genome import Genome
import re
from GenomeModel import GenomeModel
from TreeView import TreeView
from FeatureList import FeatureList
from Feature import Feature
class Search(object):
    """contains search moduls"""


    def __init__(self,model,treeview):
        self.model = model
        self.treeview = treeview

    def regexsearch(self, patterns):
        """search in a string with a re"""
        genome = Imports.genome
        regex = re.compile(patterns)
        matches = regex.finditer(genome.getSequence())
        regexlist = FeatureList("Search for: " + patterns)
        if patterns != "":
            for match in matches:
                feature = Feature("RegEx-Result at: " + str(match.start()),"Gene Sequence", match.start(),match.end() )
                regexlist.addFeature(feature)
            if regexlist.getLength()> 1:
                wx.MessageBox(str(regexlist.getLength())+" matches found!", style=wx.OK)
                Imports.con.addFeatureList(regexlist)
                Imports.con.setChanged()
                #TreeView.AddTreeNodes(self.treeview.searchResults, matches)
            else: wx.MessageBox("No matches found!", style=wx.OK)
        else: wx.MessageBox("Please enter a regular expression!", style=wx.OK)



    def genesearch(self, patterns):
        """search a gene by entering a sequence"""
        patterns.strip()
        if patterns != "":
            genome = Imports.genome
            searchstring = genome.getSequence()
            try:
                pos = searchstring.index(patterns)
                self.model.setRanges(pos-2500, pos+2500)
                self.model.setPosition(pos)
            except ValueError:
                wx.MessageBox("DNA sequence not found!", style=wx.OK)
        else: wx.MessageBox("Please enter a DNA sequence to find!", style=wx.OK)
