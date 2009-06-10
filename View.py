# -*- coding: utf-8 -*-
'''
Created on 27.05.2009

@author: mirco
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

class MainFrame(wx.Frame):
    
    hsize = 1024
    vsize = 800
    
    def __init__ (self):
        
        wx.Frame.__init__(self, None, -1, "Genome Viewer", size=(self.hsize, self.vsize))
        
        self.panel = wx.Panel(self, -1)
        self.panel.SetSize(size=(self.hsize, self.vsize))
        self.CreateStatusBar()        
        
        ### creating the menu ###
        file = wx.Menu()
        
        openGenome = file.Append(-1, "Open genome", "Open new genome-file")
        self.Bind(wx.EVT_MENU, self.OnOpenGenomeFile, openGenome)
        
        openGffAnnotation = file.Append(-1, "Open gff annotation", "Open new gff annotation-file")
        self.Bind(wx.EVT_MENU, self.OnOpenGffAnnotation, openGffAnnotation)
        
        openPttAnnotation = file.Append(-1, "Open ptt annotation", "Open new ptt annotation-file")
        self.Bind(wx.EVT_MENU, self.OnOpenPttAnnotation, openPttAnnotation)
        
        exit = file.Append(-1, "Exit", "Exit programm")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)        
        
        menu2 = wx.Menu()
        
        menu3 = wx.Menu()        

        menuBar = wx.MenuBar()
        menuBar.Append(file, "File")
        menuBar.Append(menu2, "Edit")
        menuBar.Append(menu3, "Help")
        self.SetMenuBar(menuBar)
                
        ### treeview ###
        self.container = Imports.con
        self.treeview = TreeView(self.panel, -1, Imports.con)
        self.container.addObserver(self.treeview)
        #self.treeview.SetSize(size=(self.hsize, self.vsize))
        
        ### genomeview ###
        self.genome = Imports.genome        
        self.genomemodel = GenomeModel()#(self.genome, self.features)
        self.genomemodel.setGenome(self.genome)
        self.genomemodel.setFeatureListContainer(self.container)
        self.genomeview = GenomeView(self.genomemodel, self.panel, -1)
        self.genome.addObserver(self.genomeview)
        
        ### sizer ###
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.treeview, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.genomeview, 1, wx.EXPAND | wx.ALL, 5)
        
        #hbox.Add(self.genomeview, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(hbox) 
        self.Centre()
        self.Show(True)
                
    def OnExit(self, event):
        self.Close()
    
    def OnOpenGenomeFile(self, event):
        wildcard = "FastA file (*.fasta) |*.fasta|" \
                    "FastA file (*.faa) |*.faa|" \
                    "All files (*.*) |*.*|"
        dialog = wx.FileDialog(None, "Choose a genome-file", os.getcwd(),
                               "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            fasta = Imports.Fasta()
            fasta.importfasta(dialog.GetPath())
            dialog.Destroy()  
        
    def OnOpenGffAnnotation(self, event):
        wildcard = "GFF file (*.gff) |*.gff|" \
                    "All files (*.*) |*.*|"
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
        dialog = wx.FileDialog(None, "Choose an annotation-file", os.getcwd(),
                               "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            ptt = Imports.Ptt()
            ptt.importptt(dialog.GetPath())
            dialog.Destroy()
            #print Imports.con.getPTTContainer()[2].getEnd()


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()
    
    