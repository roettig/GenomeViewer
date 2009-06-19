# -*- coding: utf-8 -*-
#import Feature
#import Tupel
from os import *
from Genome import Genome
from FeatureListContainer import FeatureListContainer
from Feature import Feature
from FeatureList import FeatureList

con = FeatureListContainer()
genome = Genome()

class Fasta(object):
    """Imports a FastA-File to an internal object"""
    
    head = ""
    sequence = ""
    
    def importfasta(self, myfile):
        myfasta = file(myfile, 'r')
        #read the first line (header)
        currline = myfasta.readline()
        firstchar = currline[0]
        #is file a fasta file
        if firstchar != ">":
            print"No Fasta file given"
        else:
            self.head = currline
        #read the file
            while currline != "":
                currline = myfasta.readline()
                currline = currline.strip()
                self.sequence += currline
            # close the stream
            myfasta.close()
            #get chars to uppercase
            self.sequence = self.sequence.upper()
        genome.setSequence(self.sequence)
        
        
class Ptt(object):
    """Import, export and parse of files in ptt format"""
    name =  ""
    proteins = ""
    genomedata = []

    def __str__(self):
        return("Genome data of" + self.name)

    def searchpttgene(self, location):
        """accepts a location as integer
           and returns false if none or more than one gene
           matches this location else it returns data of the
           location (pid etc)"""
        hits = []
        for i in xrange(len(self.genomedata)):
            min ,max = self.genomedata[i][0]
            if min <= location and location <= max:
                hits.append(self.genomedata[i])
        if len(hits == 1):
            hit = hits[0]
            return hit[0],hit[3],hit[4],hit[7],hit[8]
        else:
            return False

    def importptt(self, myfile):
        """imports a ptt file and creates and internal object"""
        f = file(myfile, 'r')
        self.name = f.readline()
        self.proteins = f.readline()
        #rownames = f.readline()
        pttlist = FeatureList()
        genomedataTemp = f.readlines()
        genomedataTemp = genomedataTemp[1:]

        for eachline in genomedataTemp:
            eachline = eachline.strip()
            tmpl = eachline.split('\t')
            l = tmpl[0].split("..")
            tmpl = tmpl[1:]
            tmpl = l+tmpl
            #print "#",tmpl
            feature = Feature(tmpl[9],tmpl[9],int(tmpl[0]), int(tmpl[1]))
            pttlist.addFeature(feature)
        f.close()
                    
        con.addPTTList(pttlist)

    def exportptt(self,Ptt):
        """Exports ptt obejcts in a ptt file"""
        exportpath = path.join(r'C:\\')
        chdir(exportpath)
        mkdir('GenomeViewer Exports')
        chdir('GenomeViewer Exports')
        example = file('Example.ptt', 'a')
        example.write(self.name)
        example.write(self.proteins)
        example.writelines(self.genomedata)
        example.close()
        

class Gff(object):
    """Import, export and parse of files in gff format"""
    versline = ""
    versline2 = ""
    data = ""
    name = ""
    complete = ""
    genomedata = []
    temp = []
    
    def __str__(self):
        return("Genome data of" + self.name)

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

    def importgff(self, myfile):
        """imports a gff file and creats an internal object"""
        f = file(myfile, 'r')
        #self.versline = f.readline()
        #self.versline2 = f.readline()
        #self.data = f.readline()
        #self.name = f.readline()
        
        gfflist = FeatureList("gff")
        genomedataTemp = f.readlines()
        genomedataTemp = genomedataTemp[5:]
        genomedataTemp = genomedataTemp[:len(genomedataTemp) -1]
              
        # Split lines of file
        for eachline in genomedataTemp:
            eachline = eachline.strip()
            tmpl = eachline.split('\t')
            #print "#",tmpl
            feature = Feature(tmpl[2], tmpl[8], int(tmpl[3]), int(tmpl[4]))
            gfflist.addFeature(feature)
            #print feature

        f.close()

        con.addGFFList(gfflist)

    def exportgff(self, Gff):
        """Exports gff obejcts in a gff file"""
        exportpath = path.join(r'C:\\')
        chdir(exportpath)
        mkdir('GenomeViewer Exports')
        chdir('GenomeViewer Exports')
        example = file('Example.gff', 'a')
        example.write(self.versline)
        example.write(self.versline2)
        example.write(self.data)
        example.write(self.name)
        example.write(self.complete)
        example.writelines(self.genomedataTemp)
        example.close()
















