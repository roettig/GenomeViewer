import Imports
from FeatureListContainer import FeatureListContainer
from Genome import Genome

class Search(object):

    genome = Genome()
    container = FeatureContainer()

    def searchpttgene(self, ):
        """accepts a location as integer
           and returns false if none or more than one gene
           matches this location else it returns data of the
           location (pid etc)"""
        hits = []
        for i in genome.getSequenceLength():
            min ,max = self.genomedata[i][0]
            if min <= location and location <= max:
                hits.append(self.genomedata[i])
        if len(hits == 1):
            hit = hits[0]
            return hit[0],hit[3],hit[4],hit[7],hit[8]
        else:
            return False



    def searchgffgene(self, location):
        hits = []
        for i in xrange(len(self.genomedata)):
            min ,max = self.genomedata[i][0]
            if min <= location and location <= max:
                hits.append(self.genomedata[i])
        if len(hits == 1):
            hit = hits[0]
            return hit[2],hit[3],hit[4],hit[8]
        else:
            return False
