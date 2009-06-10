# liest das Genom und die Nummerierung in die Textfelder

from Genome import Genome
from Layout import Layout
import wx
import wx.richtext as rt
from FeatureListContainer  import FeatureListContainer
from Observable import Observable

class GenomeModel(Observable):
    genome = Genome()
    featureListContainer = FeatureListContainer()
    upperCase = True
    charsPerLine = 50
    position = 0
    startRange = 0
    endRange = 500
    layout = Layout()
    def __init__(self, genome=Genome(), flc=FeatureListContainer(), initial_upperCase=True, initial_charsPerLine=50, initial_position=0, initial_startRange=0, initial_endRange=500):
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
        txtctrl.SetFont(self.layout.getSequenceFont())
        len=self.genome.getSequenceLength()
        sequence=self.genome.getSequence()
        if self.upperCase:
            sequence=sequence.upper()
        i=0
        while i + self.charsPerLine <= len:
            txtctrl.WriteText(sequence[i:i+self.charsPerLine])
            txtctrl.Newline()
            i+=self.charsPerLine
        txtctrl.WriteText(sequence[i:len])
    def writeNumeration(self, numTxtctrl, seqTxtctrl):
        numTxtctrl.SetFont(self.layout.getNumerationFont())
        i=0
        number=0
        while i<seqTxtctrl.GetNumberOfLines():
            numTxtctrl.WriteText(str(number) + "-" + str(number+seqTxtctrl.GetLineLength(i)-1))
            numTxtctrl.Newline()
            i+=1
            number+=self.charsPerLine
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
                            rta = rt.RichTextAttr()
                            rta.SetTextColour(self.layout.getFeatureListColor(iFlist))
                            rta.SetURL(description)
                            txtctrl.Bind(wx.EVT_TEXT_URL, self.onUrl)
                            txtctrl.SetStyle((self.modifyStartPos(start),self.modifyEndPos(end)), rta)
    def onUrl(self, evt):
        wx.MessageBox(evt.GetString(), "Description")
    def modifyStartPos(self, n):
        quot=n/self.charsPerLine
        return n+quot
    def modifyEndPos(self, n):
        quot=n/self.charsPerLine
        return n+quot+1