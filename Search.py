import Imports
from FeatureListContainer import FeatureListContainer
from Genome import Genome
import re
from GenomeModel import GenomeModel
class Search(object):
    """contains search moduls"""


    def __init__(self,model):
        self.model = model


    def regexsearch(self, regex):
        """search in a string with a re"""
        genome = Imports.genome
        container = Imports.con
        flist = []
        flist.append(re.findall(regex, genome.getSequence() , re.I))
        print flist


    def genesearch(self, patterns):
        """search a gene by entering a sequence"""
	patterns.strip()
        genome = Imports.genome
        searchstring = genome.getSequence()
        pos = searchstring.index(patterns)
        self.model.setRanges(pos-2000, pos+2000)
        self.model.setPosition(pos)
