# -*- coding: utf-8 -*-
#import Feature
#import Tupel
import os
from Genome import Genome
from FeatureListContainer import FeatureListContainer
from Feature import Feature
from FeatureList import FeatureList
import wx

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
            wx.MessageBox("No FastA-File given, pleasy try again","fatal import error", style=wx.OK)
            myfasta.close()
        else:
            self.head = currline
            currline = myfasta.readline()
        #read the file up to next header
            while currline != "":
                currline = currline.strip()
                self.sequence += currline
                currline = myfasta.readline()

                #print currline
            myfasta.close()
            self.sequence = self.sequence.upper()
        genome.setSequence(self.sequence)


class Ptt(object):
    """Import, export and parse of files in ptt format"""
    name =  ""
    proteins = ""
    genomedata = []

    def __str__(self):
        return("Genome data of" + self.name)

    def importptt(self, myfile):
        """imports a ptt file and creates and internal object"""
        f = file(myfile, 'r')
        if myfile.endswith('.ptt'):
            self.name = f.readline()
            self.proteins = f.readline()
            pttlist = FeatureList("ptt")
            genomedataTemp = f.readlines()
            genomedataTemp = genomedataTemp[1:]
            for eachline in genomedataTemp:
                eachline = eachline.strip()
                tmpl = eachline.split('\t')
                l = tmpl[0].split("..")
                tmpl = tmpl[1:]
                tmpl = l+tmpl
                feature = Feature(tmpl[9],tmpl[9],int(tmpl[0]), int(tmpl[1]))
                pttlist.addFeature(feature)
            f.close()
            con.addPTTList(pttlist)
        else:
            wx.MessageBox("No PTT-File given, pleasy try again","fatal import error", style=wx.OK)
            f.close()



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

    def importgff(self, myfile):
        """imports a gff file and creats an internal object"""
        f = file(myfile, 'r')
        if myfile.endswith('.gff'):
            gfflist = FeatureList("gff")
            genomedataTemp = f.readlines()
            genomedataTemp = genomedataTemp[5:]
            genomedataTemp = genomedataTemp[:len(genomedataTemp) -1]
            # Split lines of file
            for eachline in genomedataTemp:
                eachline = eachline.strip()
                tmpl = eachline.split('\t')
                feature = Feature(tmpl[2], tmpl[8], int(tmpl[3]), int(tmpl[4]))
                gfflist.addFeature(feature)
            f.close()
            con.addGFFList(gfflist)
        else:
            wx.MessageBox("No GFF-File given, pleasy try again","fatal import error", style=wx.OK)
            f.close()


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














