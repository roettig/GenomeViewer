import Imports
from FeatureListContainer import FeatureListContainer
from Genome import Genome
import re
from GenomeModel import GenomeModel
class Search(object):
    """contains search moduls"""

    def __init__(self,model):
        self.model = model


    def regexsearch(self, patterns):
        """ search in genome by regular-expression-search """
        genome = Imports.genome
        regex = re.compile(patterns , re.I)
        matches = regex.search(genome.getSequence())
        regexlist = FeatureList("regex")
        if matches is None:
            wx.MessageBox("Suchstring ist nicht vorhanden!", style=wx.OK)
        else:
            for match in matches:
                feature = Feature("Reg-Ex Hit","Gene Sequence", match.start(),match.end() )
                regexlist.addFeature(feature)
            Imports.con.addFeatureList(regexlist)



    def genesearch(self, patterns):
        """search a gene by entering a sequence"""
        patterns.strip()
        genome = Imports.genome
        searchstring = genome.getSequence()
        pos = searchstring.index(patterns)
        self.model.setRanges(pos-2000, pos+2000)
        self.model.setPosition(pos)
