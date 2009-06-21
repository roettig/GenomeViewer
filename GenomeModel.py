# liest das Genom (+Annotationen) und die Nummerierung in die Textfelder

from Genome import Genome
from Layout import Layout
import wx
import wx.richtext as rt
from FeatureListContainer  import FeatureListContainer
from Observable import Observable
from random import randrange


class GenomeModel(Observable):
    genome = Genome()
    featureListContainer = FeatureListContainer()
    upperCase = True
    charsPerLine = 0
    position = 0
    startRange = 0
    endRange = 0
    layout = Layout()
    def __init__(self, genome=Genome(), flc=FeatureListContainer(), initial_upperCase=True, initial_charsPerLine=50, initial_position=0, initial_startRange=0, initial_endRange=10000):
        self.genome=genome
        self.featureListContainer=flc
        self.upperCase=initial_upperCase
        self.charsPerLine=initial_charsPerLine
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
    def getUpperCase(self):
        return self.upperCase
    def setUpperCase(self, bool):
        self.upperCase=bool
        self.setChanged()
    def getCharsPerLine(self):
        return self.charsPerLine
    def setCharsPerLine(self, n):
        self.charsPerLine=n
        self.setChanged()
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
    def writeSequence(self, txtctrl):
        if self.upperCase:
            sequence=self.genome.getSequence()[self.startRange:self.endRange].upper()
        else:
            self.genome.getSequence()[self.startRange:self.endRange]
        seqLen=len(sequence)
        numeration=self.startRange
        i=0
        while i+self.charsPerLine <= seqLen:
            txtctrl.BeginStyle(self.layout.getSeqTextAttrEx())
            # print str(len(sequence[i:i+self.charsPerLine]))
            txtctrl.WriteText(sequence[i:i+self.charsPerLine])
            txtctrl.EndStyle()
            txtctrl.Newline()
            txtctrl.BeginStyle(self.layout.getNumTextAttrEx())
            txtctrl.WriteText(self.writeNum(len(str(self.endRange-1)), str(numeration), str(numeration+txtctrl.GetLineLength(txtctrl.GetNumberOfLines()-2)-1)))
            txtctrl.EndStyle()
            # letzte Zeile ohne Newline()
            if i+self.charsPerLine < seqLen:
                # print "charsPerLine" + str(i+self.charsPerLine) + "=" + str(seqLen)
                txtctrl.Newline()
            i+=self.charsPerLine
            numeration+=txtctrl.GetLineLength(txtctrl.GetNumberOfLines()-3)
        if seqLen-i>0:
            txtctrl.BeginStyle(self.layout.getSeqTextAttrEx())
            txtctrl.WriteText(sequence[i:])
            txtctrl.EndStyle()
            txtctrl.Newline()
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
        rta = rt.RichTextAttr()
        #Farbgebung
        self.layout.addTypeColDict(type)
        rta.SetTextColour(self.layout.getTypeColDict(type))
        rta.SetURL(description)
        txtctrl.Bind(wx.EVT_TEXT_URL, self.onUrl)
        #txtctrl.SetStyle((246, 306), rta)
        modulo=start%self.charsPerLine
        modStart=self.modifyStartPos(start,txtctrl)
        modEnd=self.modifyEndPos(end, txtctrl)
        # Anfang: wenn Einfaerbung nicht am Zeilenanfang beginnt
        if modulo!=0:
            diff=self.charsPerLine-modulo
            txtctrl.SetStyle((modStart,modStart+diff), rta)
            modStart+=diff+txtctrl.GetLineLength(1)+2
        # Mitte: faerbt ganze Zeilen
        while modStart+self.charsPerLine<=modEnd:
            txtctrl.SetStyle((modStart,modStart+self.charsPerLine), rta)
            #print str(modStart+self.charsPerLine+txtctrl.GetLineLength(1)+1)
            modStart+=self.charsPerLine+txtctrl.GetLineLength(1)+2
        # Ende: faerbt letzte Zeile nicht ganz
        if modEnd-modStart>0:
            txtctrl.SetStyle((modStart,modEnd), rta)
    # wandelt Positionen auf dem Genom in Positionen im Genomtextfeld um
    def modifyStartPos(self, n, txtctrl):
        newN=n-self.startRange
        quot=newN/self.charsPerLine*2
        numCount=0
        i=1
        while i <= quot:
            numCount+=txtctrl.GetLineLength(i)
            i+=2
        print newN+quot+numCount
        return newN+quot+numCount
    def modifyEndPos(self, n, txtctrl):
        newN=n-self.startRange
        quot=newN/self.charsPerLine*2
        numCount=0
        i=1
        while i < quot:
            numCount+=txtctrl.GetLineLength(i)
            i+=2
        print str(newN+quot+numCount+1)
        return newN+quot+numCount+1
    def onUrl(self, evt):
        wx.MessageBox(evt.GetString(), "Description")