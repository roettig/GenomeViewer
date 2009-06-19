#!/usr/bin/python

import wx
from GenomeView import GenomeView
from GenomeModel import GenomeModel
from Genome import Genome
from Feature import Feature
from FeatureList import FeatureList
from FeatureListContainer import FeatureListContainer


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,400))

        genome = Genome()
        genome.setSequence("")

        featurelist=FeatureList("test")
        feature1=Feature("protein1", "protein asdgqiuw", 0, 49)
        feature2=Feature("protein2", "asdgqidu", 270, 300)
        featurelist.addFeature(feature1)
        featurelist.addFeature(feature2)

        gff=FeatureList("gff")
        featuregff1=Feature("protein1", "protein asdgqiuw", 60, 70)
        featuregff2=Feature("protein1", "protein asdgqiuw", 78, 80)
        gff.addFeature(featuregff1)
        gff.addFeature(featuregff2)

        flc=FeatureListContainer()
        flc.addFeatureList(featurelist)
        flc.addFeatureList(gff)
        self.model = GenomeModel()
        self.model.setGenome(genome)
        self.model.setFeatureListContainer(flc)
        self.view = GenomeView(self.model, self)
        self.Show()

app = wx.App()
frame = MainFrame(None, -1, 'Genome View')
app.MainLoop()