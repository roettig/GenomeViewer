import Imports
from FeatureListContainer import FeatureListContainer
from Genome import Genome
import re

class Search(object):

    genome = Genome()
    container = FeatureListContainer()

    def regexsearch(self, regex):
        """search in a string with a re"""
        genome = Genome()
        container = FeatureListContainer()
        print genome.getSequence()
        flist = []
        flist.append(re.findall(regex, genome.getSequence() , re.I))
        print flist
