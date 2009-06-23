# -*- coding: utf-8 -*-
'''
Created on 27.05.2009

@author: mirco,phil
'''
import wx
import os
from FeatureListContainer import FeatureListContainer
from Genome import Genome
from GenomeView import GenomeView
from GenomeModel import GenomeModel
from IObserver import IObserver
from TreeView import TreeView
import Imports
from Search import Search

class MainFrame(wx.Frame):

    hsize = 1024
    vsize = 800

    def __init__ (self):

        wx.Frame.__init__(self, None, -1, "Genome Viewer", size=(self.hsize, self.vsize))
        #self.panel = wx.Panel(self, -1)
        #self.panel.SetSize(size=(self.hsize, self.vsize))

        # macht, dass nummerierung noch nicht losgeht, bevor genom geladen ist
        loaded = False

        self.CreateStatusBar()

        ### creating the menu ###
        file = wx.Menu()
        editmenu = wx.Menu()
        helpmenu = wx.Menu()
        searchmenu = wx.Menu()
        selecmenu = wx.Menu()

        menuBar = wx.MenuBar()


        menuBar.Append(file, "File")
        #menuBar.Append(editmenu, "Edit")
        menuBar.Append(searchmenu, "Search")
        menuBar.Append(selecmenu, "Feature Selection")
        menuBar.Append(helpmenu, "Help")


        openGenome = file.Append(-1, "Open genome", "Open new genome-file")
        self.Bind(wx.EVT_MENU, self.OnOpenGenomeFile, openGenome)

        openGffAnnotation = file.Append(-1, "Open GFF annotation", "Open new gff annotation-file")
        self.Bind(wx.EVT_MENU, self.OnOpenGffAnnotation, openGffAnnotation)

        openPttAnnotation = file.Append(-1, "Open PTT annotation", "Open new ptt annotation-file")
        self.Bind(wx.EVT_MENU, self.OnOpenPttAnnotation, openPttAnnotation)

        exit = file.Append(-1, "Exit", "Exit programm")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        openSearch = searchmenu.Append(-1, "regular expression", "Search with regular expressions")
        self.Bind(wx.EVT_MENU, self.OnOpenSearch, openSearch)

        self.SetMenuBar(menuBar)


        self.container = Imports.con
	self.genome = Imports.genome
        self.genomemodel = GenomeModel()#(self.genome, self.features)
        self.genomemodel.setGenome(self.genome)
        self.genomemodel.setFeatureListContainer(self.container)
	
	### treeview ###
        self.treeview = TreeView(self, -1, self.container, self.genomemodel)
        self.container.addObserver(self.treeview)
        #self.treeview.SetSize(size=(self.hsize, self.vsize))

        ### genomeview ###
        self.genomeview = GenomeView(self.genomemodel, self, -1)
        # brauchen wir das? dafür gibts doch die updateFkt
        # if(loaded == True):
        #    self.genomeview.write()
        self.genome.addObserver(self.genomeview)

        ### sizer ###
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.treeview, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.genomeview, 1, wx.EXPAND | wx.ALL, 5)

        #hbox.Add(self.genomeview, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(hbox)
        self.Centre()
        self.Show(True)

    def OnExit(self, event):
        self.Close()

    def OnOpenGenomeFile(self, event):
        wildcard = "FastA file (*.fna) |*.fna|" \
		    "FastA file (*.fasta) |*.fasta|" \
                    "FastA file (*.faa) |*.faa|" \
                    "All files (*.*) |*.*|"
        #wildcard=""
        dialog = wx.FileDialog(None, "Choose a genome-file", os.getcwd(),
                               "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            fasta = Imports.Fasta()
            fasta.importfasta(dialog.GetPath())
            dialog.Destroy()

        self.loaded = True

    def OnOpenGffAnnotation(self, event):
        wildcard = "GFF file (*.gff) |*.gff|" \
                    "All files (*.*) |*.*|"
        #wildcard=""
        dialog = wx.FileDialog(None, "Choose an annotation-file", os.getcwd(),
                               "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            gff = Imports.Gff()
            gff.importgff(dialog.GetPath())
            dialog.Destroy()
            #print Imports.con.getGFFContainer()[2].getEnd()

    def OnOpenPttAnnotation(self, event):
        wildcard = "PTT file (*.ptt) |*.ptt|" \
                    "All files (*.*) |*.*|"
        #wildcard=""
        dialog = wx.FileDialog(None, "Choose an annotation-file", os.getcwd(),
                               "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            ptt = Imports.Ptt()
            ptt.importptt(dialog.GetPath())
            dialog.Destroy()
            #print Imports.con.getPTTContainer()[2].getEnd()

    def OnOpenSearch(self,event):
        dialog = wx.TextEntryDialog(None, "Please enter regular expression here:",
                                    "Regular Expression Search","",
                                    style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            print "You have entered: %s" % dialog.GetValue()
            search=Search()
            search.regexsearch(dialog.GetValue())

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()

