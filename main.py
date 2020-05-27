#Este es el main del proyecto
from BraiNerdPanel import BraiNerdPanel
from Electrodos import Electrodos
import wx
import wx.lib.agw.fourwaysplitter as fws
from numpy import arange, sin, pi

#Main manda llamar todos los demas modulos de python para que sean visibles y anadidos al procesamiento necesario para el correcto funcionamiento del programa.
class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = "Brainerds",size = (1000,800))
        splitter = wx.SplitterWindow(self)
        splitterTABD = fws.FourWaySplitter(splitter)
        self.electrodos = Electrodos()

        self.thetaPanel = BraiNerdPanel(splitterTABD,)
        self.alphaPanel = BraiNerdPanel(splitterTABD,)
        self.betaPanel = BraiNerdPanel(splitterTABD,)
        self.deltaPanel = BraiNerdPanel(splitterTABD,)

        self.menuPanel = BraiNerdPanel(splitter)
        splitter.SplitHorizontally(self.menuPanel, splitterTABD)

        splitterTABD.AppendWindow(self.thetaPanel)
        splitterTABD.AppendWindow(self.alphaPanel)
        splitterTABD.AppendWindow(self.betaPanel)
        splitterTABD.AppendWindow(self.deltaPanel)
        splitter.SetMinimumPaneSize(120)


        self.menuPanel.ShowMenuPanel()
        self.thetaPanel.ShowThetaPanel(self.electrodos.GetAngleElectrode(),self.electrodos.GetRElectrode())
        self.alphaPanel.ShowAlphaPanel(self.electrodos.GetAngleElectrode(),self.electrodos.GetRElectrode())
        self.betaPanel.ShowBetaPanel(self.electrodos.GetAngleElectrode(),self.electrodos.GetRElectrode())
        self.deltaPanel.ShowDeltaPanel(self.electrodos.GetAngleElectrode(),self.electrodos.GetRElectrode())
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.TimeInterval, self.timer)
        self.timer.Start(6)

        self.wave = 0

    def TimeInterval(self, event):
        self.wave += 3*pi/360
        self.thetaPanel.UpdateValues(self.wave)
        self.alphaPanel.UpdateValues(self.wave)
        self.betaPanel.UpdateValues(self.wave)
        self.deltaPanel.UpdateValues(self.wave)
        self.menuPanel.UpdateMenu()
        #print (self.menuPanel.GetSize())


#Comprueba que este archivo sea el main ejecutable para poder ejecutarlo
if __name__ == "__main__":
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()


"""
extension = 96 lineas
densidad de defectos = 1/96
tiempo para corregir defectos = aproximadamente 1/2 hora
porcentaje libre de defectos = 25%
dedicacion = 8/2 = 4
productividad = 96 / 8 = 12

"""