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
from GenomeBar import GenomeBar
from IObserver import IObserver
from TreeView import TreeView
import Imports
from Search import Search
from wx.lib.wordwrap import wordwrap
from ProportionalSplitter import ProportionalSplitter
from sys import platform
from CheckBoxFrame import CheckBoxFrame

class MainFrame(wx.Frame):

    hsize = 800
    vsize = 600

    def __init__ (self):

        wx.Frame.__init__(self, None, -1, "Genome Viewer", size=(self.hsize, self.vsize))
        #self.panel = wx.Panel(self, -1)
        #self.panel.SetSize(size=(self.hsize, self.vsize))

        # macht, dass nummerierung noch nicht losgeht, bevor genom geladen ist
        # loaded = False

        self.CreateStatusBar()
        self.MakeMenuBar()

        self.container = Imports.con
        self.genome = Imports.genome
        self.genomemodel = GenomeModel()#(self.genome, self.features)
        self.genomemodel.setGenome(self.genome)
        self.genomemodel.setFeatureListContainer(self.container)
        
        ### splitter ###
        self.splitLeft = ProportionalSplitter(self, -1, 0.33)
        self.splitRight = ProportionalSplitter(self.splitLeft, -1, 0.9)
        
	    ### treeview ###
        self.treeview = TreeView(self.container, self.genomemodel, self.splitLeft)
        self.container.addObserver(self.treeview)

        ### genomeview ###
        self.genomeview = GenomeView(self.genomemodel, self.splitRight)
        self.genome.addObserver(self.genomeview)

	    ### genomebar ###
        self.genomebar = GenomeBar(self.genomemodel, self.splitRight)
        
        self.splitLeft.SplitVertically(self.treeview,self.splitRight)
        self.splitRight.SplitHorizontally(self.genomeview, self.genomebar)

        ### sizer ###
#        sizer = wx.GridBagSizer(15,20)
#        sizer.Add(self.treeview, (0, 0), (15, 5), wx.EXPAND | wx.LEFT | wx.TOP | wx.BOTTOM , 5)
#        sizer.Add(self.genomeview, (0, 5),(12, 15), wx.EXPAND | wx.RIGHT | wx.TOP , 5)
#        sizer.Add(self.genomebar, (12, 5),(3, 15), wx.EXPAND | wx.RIGHT | wx.BOTTOM , 5)
#
#        sizer.AddGrowableCol(19)
#        sizer.AddGrowableRow(10)
#
#        self.SetSizerAndFit(sizer)

        self.Centre()
        self.Show(True)


    def MakeMenuBar(self):
        ''' creating the menu '''
        #menu "File
        fileMenu = wx.Menu()
        # menu item "Open Genome"
        openGenome = fileMenu.Append(-1, "Open genome", "Open new genome-file")
        self.Bind(wx.EVT_MENU, self.OnOpenGenomeFile, openGenome)
        # menu item "Open PTT annotation"
        openPttAnnotation = fileMenu.Append(-1, "Open PTT annotation", "Open new ptt annotation-file")
        self.Bind(wx.EVT_MENU, self.OnOpenPttAnnotation, openPttAnnotation)
        # menu item "Open GFF annotation"
        openGffAnnotation = fileMenu.Append(-1, "Open GFF annotation", "Open new gff annotation-file")
        self.Bind(wx.EVT_MENU, self.OnOpenGffAnnotation, openGffAnnotation)

        fileMenu.AppendSeparator()
        # menu item "Exit"
        exit = fileMenu.Append(-1, "Exit", "Exit programm")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        #menu "Edit
        editMenu = wx.Menu()
        edit = editMenu.Append(-1, "Edit", "Edit Feature Selection")
        self.Bind(wx.EVT_MENU, self.OnOpenCheckFrame, edit)



        #menu SearchMenu
        searchMenu = wx.Menu()
        # menu item
        openRegExSearch = searchMenu.Append(-1, "regular expression", "Search with regular expressions")
        self.Bind(wx.EVT_MENU, self.OnOpenRegExSearch, openRegExSearch)

        # menu item
        openGeneSearch = searchMenu.Append(-1, "Gene finding", "Search with sequence string")
        self.Bind(wx.EVT_MENU, self.OnOpenGeneSearch, openGeneSearch)



        #self.Bind(wx.EVT_MENU, self.onOpenFeatureSelection, openFeatureSelection)
        #menu Properties
        propertiesMenu = wx.Menu()
        # menu item
        setseqfont = propertiesMenu.Append(-1, "Sequence Font", "Set Sequence Font")
        self.Bind(wx.EVT_MENU, self.OnSetSeqFont, setseqfont)
        # menu item
        setnumfont = propertiesMenu.Append(-1, "Numeration Font", "Set Numeration Font")
        self.Bind(wx.EVT_MENU, self.OnSetNumFont, setnumfont)

        #menu Help
        helpMenu = wx.Menu()
        # menu item
        about = helpMenu.Append(-1, "About", "About GenomeViewer")
        self.Bind(wx.EVT_MENU, self.OnAbout, about)

        #NCBI
        stuff = helpMenu.Append(-1, "Stuff", "Get more Stuff to View")
        self.Bind(wx.EVT_MENU, self.OnStuff, stuff)

        #append items to menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")
        menuBar.Append(searchMenu, "Search")
        #menuBar.Append(featureselectMenu, "Feature Selection")
        menuBar.Append(propertiesMenu, "Properties")
        menuBar.Append(helpMenu, "Help")
        self.SetMenuBar(menuBar)


    def OnOpenCheckFrame(self, evt):
        check = CheckBoxFrame()


    def OnSetSeqFont(self, evt):
        dlg = wx.FontDialog(self, wx.FontData())
        dlg.GetFontData().SetInitialFont(self.genomemodel.getSeqFont())
        if dlg.ShowModal() == wx.ID_OK:
            self.genomemodel.setSeqFont(dlg.GetFontData().GetChosenFont())
        dlg.Destroy()

    def OnSetNumFont(self, evt):
        dlg = wx.FontDialog(self, wx.FontData())
        dlg.GetFontData().SetInitialFont(self.genomemodel.getNumFont())
        if dlg.ShowModal() == wx.ID_OK:
            self.genomemodel.setNumFont(dlg.GetFontData().GetChosenFont())
        dlg.Destroy()

    def OnAbout(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "GenomeViewer"
        info.Version = "1.0"
        info.Copyright = "(C) 2009"
        info.Description = wordwrap(
            "A \"GenomeViewer\" is a software program that views genome sequences ",
            350, wx.ClientDC(self))
        info.WebSite = ("http://www.uni-tuebingen.de", "Our home page")
        info.Developers = [ "Mirco",
                            "Phil",
                            "Julian",
                            "Matze" ]
        licenseText = "Everybody is free, so everything is free...."
        info.Licence = wordwrap(licenseText, 500, wx.ClientDC(self))
        wx.AboutBox(info)

    def OnExit(self, event):
        self.Close()

    def OnOpenGenomeFile(self, event):
        if platform == "win32":
            wildcard = ""
        else:
            wildcard="*"
        dialog = wx.FileDialog(None, "Choose a genome-file", os.getcwd(),
                               "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            fasta = Imports.Fasta()
            fasta.importfasta(dialog.GetPath())
            dialog.Destroy()

        # self.loaded = True

    def OnOpenGffAnnotation(self, event):
        if platform == "win32":
            wildcard = ""
        else:
            wildcard="*"
        dialog = wx.FileDialog(None, "Choose an GFF-annotation-file", os.getcwd(),
                               "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            gff = Imports.Gff()
            gff.importgff(dialog.GetPath())
            dialog.Destroy()
            #print Imports.con.getGFFContainer()[2].getEnd()

    def OnOpenPttAnnotation(self, event):
        if platform == "win32":
            wildcard = ""
        else:
            wildcard="*"
        dialog = wx.FileDialog(None, "Choose an PTT-annotation-file", os.getcwd(),
                               "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            ptt = Imports.Ptt()
            ptt.importptt(dialog.GetPath())
            dialog.Destroy()
            #print Imports.con.getPTTContainer()[2].getEnd()

    def OnOpenRegExSearch(self,event):
        dialog = wx.TextEntryDialog(None, "Please enter regular expression here:",
                                    "Regular Expression Search","",
                                    style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            print "You have entered: %s" % dialog.GetValue()
            search=Search(self.genomemodel)
            search.regexsearch(dialog.GetValue())

    def OnOpenGeneSearch(self,event):
        dialog = wx.TextEntryDialog(None, "Please enter sequence string here:",
                                    "Gene finding","",
                                    style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            print "You have entered: %s" % dialog.GetValue()
            search=Search(self.genomemodel)
            search.genesearch(dialog.GetValue())

    def OnStuff(self,event):
        info = wx.AboutDialogInfo()
        info.Name = "NCBI"
        info.Description = wordwrap(
            "to get more crazy stuff for GenView....click",
            350, wx.ClientDC(self))
        info.WebSite = ("http://www.ncbi.nlm.nih.gov/", "Homepage of NCBI")
        wx.AboutBox(info)



if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()

