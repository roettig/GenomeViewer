# -*- coding: utf-8 -*-
# liest das Genom (+Annotationen) und die Nummerierung in die Textfelder

from Genome import Genome
from Layout import Layout
import wx
import wx.richtext as rt
from FeatureListContainer  import FeatureListContainer
from Observable import Observable
from random import randrange
from Information import Information


class GenomeModel(Observable):
    genome = Genome()
    featureListContainer = FeatureListContainer()
    position = 0
    startRange = 0
    endRange = 0
    layout = Layout()
    def __init__(self, genome=Genome(), flc=FeatureListContainer(), initial_position=3520, initial_startRange=0, initial_endRange=5000):
        self.genome=genome
        self.featureListContainer=flc
        self.position=initial_position
        self.startRange=initial_startRange
        self.endRange=initial_endRange
        self.layout=Layout()
    def getGenome(self):
        return self.genome
    def setGenome(self, genome):
        self.genome=genome
        self.setChanged()
    def getFeatureListContainer(self):
        return self.featureListContainer
    def setFeatureListContainer(self, flc):
        self.featureListContainer=flc
        self.setChanged()
    def getCharsPerLine(self):
        return self.layout.getCharsPerLine()
    def setCharsPerLine(self, n):
        self.layout.setCharsPerLine(n)
    def getPosition(self):
        return self.position
    def setPosition(self, n):
        self.position=n
        self.setChanged()
    def getStartRange(self):
        return self.startRange
    def setStartRange(self, n):
        self.startRange=n
        self.setChanged()
    def getEndRange(self):
        return self.endRange
    def setEndRange(self, n):
        self.endRange=n
        self.setChanged()
    def setRanges(self, start ,end):
        self.startRange = start
        self.endRange = end
        self.setChanged()
    def resetLayout(self):
        new = Layout()
        self.layout = Layout()
        self.setChanged()
    def getTypeDict(self):
        return self.layout.getTypeDict()
    def getNumSize(self):
        return self.layout.getNumSize()
    def incNumSize(self, int):
        numsize=self.layout.getNumSize()
        self.layout.setNumSize(numsize+int)
    def decNumSize(self, int):
        numsize=self.layout.getNumSize()
        if (numsize-int >=0):
            self.layout.setNumSize(numsize-int)
        else:
            self.layout.setNumSize(0)
    def getSeqSize(self):
        return self.layout.getSeqSize();
    def incSeqSize(self, int):
        seqsize=self.layout.getSeqSize()
        self.layout.setSeqSize(seqsize+int)
    def decSeqSize(self, int):
        seqsize=self.layout.getSeqSize()
        if (seqsize-int >=0):
            self.layout.setSeqSize(seqsize-int)
        else:
            self.layout.setSeqSize(0)
    def isItalic(self):
        return self.layout.getSeqStyle() == wx.ITALIC
    def isBold(self):
        return self.layout.getSeqWeight() == wx.BOLD
    def changeSeqWeight(self):
        if self.layout.getSeqWeight()== wx.NORMAL:
            self.layout.setSeqWeight(wx.BOLD)
        else:
            self.layout.setSeqWeight(wx.NORMAL)
    def changeSeqStyle(self):
        if self.layout.getSeqStyle()== wx.NORMAL:
            self.layout.setSeqStyle(wx.ITALIC)
        else:
            self.layout.setSeqStyle(wx.NORMAL)
    def increaseLineSp(self, int):
        lp=self.layout.getLineSpacing()
        self.layout.setLineSpacing(lp+int)
    def decreaseLineSp(self, int):
        lp=self.layout.getLineSpacing()
        if lp-int >= 0:
            self.layout.setLineSpacing(lp-int)
        else:
            self.layout.setLineSpacing(0)
    def indentMore(self, int):
        indent=self.layout.getLeftIndent()
        self.layout.setLeftIndent(indent+int)
    def indentLess(self, int):
        indent=self.layout.getLeftIndent()
        if indent-int>=0:
            self.layout.setLeftIndent(indent-int)
        else:
            self.layout.setLeftIndent(0)
    def setSeqColor(self, color):
        self.layout.setSeqColor(color)
    def getSeqColor(self):
        return self.layout.getSeqColor()
    def setNumColor(self, color):
        self.layout.setNumColor(color)
    def getNumColor(self):
        return self.layout.getNumColor()
    def isUpperCase(self):
        return self.layout.getUpperCase()
    def changeUpperCase(self):
        if self.layout.getUpperCase():
            self.layout.setUpperCase(False)
        else:
            self.layout.setUpperCase(True)
    def getCharWidth(self):
        self.layout.getCharWidth()
    def writeSequence(self, txtctrl):
        #print self.genome.getSequence()[0:50]
        #print "UpperCase: " + str(self.layout.getUpperCase())
        if self.layout.getUpperCase():
            sequence=self.genome.getSequence()[self.startRange:self.endRange].upper()
        else:
            sequence=self.genome.getSequence()[self.startRange:self.endRange].lower()
        seqLen=len(sequence)
        numeration=self.startRange
        i=0
        while i+self.layout.getCharsPerLine() <= seqLen:
            txtctrl.BeginStyle(self.layout.getSeqTextAttrEx())
            # print str(len(sequence[i:i+self.charsPerLine]))
            txtctrl.WriteText(sequence[i:i+self.layout.getCharsPerLine()])
            txtctrl.Newline()
            txtctrl.EndStyle()
            txtctrl.BeginStyle(self.layout.getNumTextAttrEx())
            txtctrl.WriteText(self.writeNum(len(str(self.endRange-1)), str(numeration), str(numeration+txtctrl.GetLineLength(txtctrl.GetNumberOfLines()-2)-1)))
            # letzte Zeile ohne Newline()
            if i+self.layout.getCharsPerLine() < seqLen:
                # print "charsPerLine" + str(i+self.charsPerLine) + "=" + str(seqLen)
                txtctrl.Newline()
            txtctrl.EndStyle()
            i+=self.layout.getCharsPerLine()
            numeration+=txtctrl.GetLineLength(txtctrl.GetNumberOfLines()-3)
        if seqLen-i>0:
            txtctrl.BeginStyle(self.layout.getSeqTextAttrEx())
            txtctrl.WriteText(sequence[i:])
            txtctrl.Newline()
            txtctrl.EndStyle()
            txtctrl.BeginStyle(self.layout.getNumTextAttrEx())
            txtctrl.WriteText(self.writeNum(len(str(self.endRange)), str(numeration), str(numeration+txtctrl.GetLineLength(txtctrl.GetNumberOfLines()-2))))
            txtctrl.EndStyle()
    # gibt Nummerierung als gleichlange Strings zurueck
    def writeNum(self, strLen, str1, str2):
        while len(str1) < strLen:
            str1= "0" + str1
        while len(str2) < strLen:
            str2= "0" + str2
        return str1 + "-" + str2
    # durchsucht den Container nach allen aktiven Features und uebergibt deren Parameter an writeFeaturesHelper
    def writeFeatures(self, txtctrl):
        for iFlist in range(self.featureListContainer.getContainerLength()):
            # print iFlist
            # print self.featureListContainer.getContainerLength()
            if self.featureListContainer.getFlistActive(iFlist):
                for iFeature in range(self.featureListContainer.getFlistLength(iFlist)):
                    # print iFeature
                    # print self.featureListContainer.getFlistLength(iFlist)
                    if self.featureListContainer.getFeatureActive(iFlist, iFeature):
                        start=self.featureListContainer.getStartPos(iFlist, iFeature)
                        end=self.featureListContainer.getEndPos(iFlist, iFeature)
                        if start >= self.startRange and end <= self.endRange:
                            type=self.featureListContainer.getType(iFlist, iFeature)
                            description=self.featureListContainer.getDescription(iFlist, iFeature)
                            self.writeFeaturesHelper(txtctrl, start, end, type, description)
    # faerbt Bereiche und ueberspringt Nummerierung
    def writeFeaturesHelper(self, txtctrl, start, end, type, description):
        #print "start1: " + str(start)
        #print "end1: " + str(end)
        rta = rt.RichTextAttr()
        #Farbgebung
        self.layout.addTypeColDict(type)
        rta.SetTextColour(self.layout.getTypeColDict(type))
        description=description+";"+str(start)+";"+str(end)+";"+type
        rta.SetURL(description)
        txtctrl.Bind(wx.EVT_TEXT_URL, self.onUrl)
        #txtctrl.SetStyle((246, 306), rta)
        calc1=start%self.layout.getCharsPerLine()
        calc2=self.layout.getCharsPerLine()-calc1
        calc3=self.startRange%self.layout.getCharsPerLine()
        calc4=(calc2+calc3)%self.layout.getCharsPerLine()
        modStart=self.modifyStartPos(start,txtctrl)
        modEnd=self.modifyEndPos(end, txtctrl)
        #print "calc1: " + str(calc1)
        #print "calc2: " + str(calc2)
        #print "calc3: " + str(calc3)
        #print "calc4: " + str(calc4)
        #print "start2: " + str(modStart)
        #print "end2: " + str(modEnd)
        # Anfang: wenn Einfaerbung nicht am Zeilenanfang beginnt
        if calc4!=0:
            if end-start<=calc4:
                txtctrl.SetStyle((modStart,modEnd), rta)
                modStart+=modEnd
                #print "if"
            else:
                txtctrl.SetStyle((modStart,modStart+calc4), rta)
                modStart+=calc4+txtctrl.GetLineLength(1)+2
                #print "else"
        # Mitte: faerbt ganze Zeilen
        while modStart+self.layout.getCharsPerLine()<=modEnd:
            txtctrl.SetStyle((modStart,modStart+self.layout.getCharsPerLine()), rta)
            #print str(modStart+self.charsPerLine+txtctrl.GetLineLength(1)+1)
            modStart+=self.layout.getCharsPerLine()+txtctrl.GetLineLength(1)+2
            #print "middle"
        # Ende: faerbt letzte Zeile nicht ganz
        if modEnd-modStart>0:
            txtctrl.SetStyle((modStart,modEnd), rta)
            #print "end"
    # wandelt Positionen auf dem Genom in Positionen im Genomtextfeld um
    def modifyStartPos(self, n, txtctrl):
        newN=n-self.startRange
        quot=newN/self.layout.getCharsPerLine()*2
        numCount=0
        i=1
        while i <= quot:
            numCount+=txtctrl.GetLineLength(i)
            i+=2
        #print newN+quot+numCount
        return newN+quot+numCount
    def modifyEndPos(self, n, txtctrl):
        newN=n-self.startRange
        quot=newN/self.layout.getCharsPerLine()*2
        numCount=0
        i=1
        while i < quot:
            numCount+=txtctrl.GetLineLength(i)
            i+=2
        #print str(newN+quot+numCount+1)
        return newN+quot+numCount+1

    def onUrl(self, evt):
        info = Information(None, -1, evt.GetString(), 'Information')
        info.ShowModal()
        info.Destroy()
        #wx.MessageBox(evt.GetString(), "Description")

    # rechnet Position im Genom in Position im Textfeld um und scrollt im Textfeld an richtige Stelle
    def showPos(self, txtctrl):
        if self.position>=self.startRange and self.position<=self.endRange:
            realPos=self.modifyStartPos(self.position, txtctrl)
            txtctrl.ShowPosition(realPos)
            txtctrl.SelectWord(realPos)
    # rechnet Position des Features in Position im Textfeld um und scrollt im Textfeld an richtige Stelle
    def showFeature(self, start, end, txtctrl):
        realStart=self.modifyStartPos(start, txtctrl)
        realEnd=self.modifyEndPos(end, txtctrl)
        txtctrl.ShowPosition(realStart)
        txtctrl.SetSelection(realStart, realEnd)