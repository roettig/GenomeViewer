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


    def __init__(self,model):
        self.model = model


    def regexsearch(self, patterns):
        """search in a string with a re"""
        genome = Imports.genome
        regex = re.compile(patterns)
        matches = regex.finditer(genome.getSequence())
        regexlist = FeatureList("regex")
        if matches is None:
            wx.MessageBox("Suchstring ist nicht vorhanden!", style=wx.OK)
        else:
            for match in matches:
                feature = Feature("Reg-Ex Hit","Gene Sequence", match.start(),match.end() )
                regexlist.addFeature(feature)
            Imports.con.addFeatureList(regexlist)
            TreeView.AddTreeNodes(TreeView.tree.searchResults, matches)




    def genesearch(self, patterns):
        """search a gene by entering a sequence"""
        patterns.strip()
        genome = Imports.genome
        searchstring = genome.getSequence()
        pos = searchstring.index(patterns)
        self.model.setRanges(pos-2500, pos+2500)
        self.model.setPosition(pos)
