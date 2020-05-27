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
        self.splitterTABD = fws.FourWaySplitter(splitter)
        self.electrodos = Electrodos()

        self.thetaPanel = BraiNerdPanel(self.splitterTABD,)
        self.alphaPanel = BraiNerdPanel(self.splitterTABD,)
        self.betaPanel = BraiNerdPanel(self.splitterTABD,)
        self.deltaPanel = BraiNerdPanel(self.splitterTABD,)

        self.menuPanel = BraiNerdPanel(splitter)
        splitter.SplitHorizontally(self.menuPanel, self.splitterTABD)

        self.splitterTABD.AppendWindow(self.thetaPanel)
        self.splitterTABD.AppendWindow(self.alphaPanel)
        self.splitterTABD.AppendWindow(self.betaPanel)
        self.splitterTABD.AppendWindow(self.deltaPanel)
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

        self.Bind(wx.EVT_BUTTON, self.OnButtonClickInicio, self.menuPanel.InicioButton()) 
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickConfiguracion, self.menuPanel.ConfiguracionButton()) 
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickGuardar,self.menuPanel.GuardarButton()) 
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickPuntos,self.menuPanel.PuntosMonButton())
        self.thetaPanel.GetCanvas().mpl_connect('button_press_event', self.OnClickThetaPanel)
        self.alphaPanel.GetCanvas().mpl_connect('button_press_event', self.OnClickAlphaPanel)
        self.betaPanel.GetCanvas().mpl_connect('button_press_event', self.OnClickBetaPanel)
        self.deltaPanel.GetCanvas().mpl_connect('button_press_event', self.OnClickDeltaPanel)
        self.thetaPanel.ShowMinimizarButton()
        self.alphaPanel.ShowMinimizarButton()
        self.betaPanel.ShowMinimizarButton()
        self.deltaPanel.ShowMinimizarButton()


    def OnButtonClicMinimizar(self, event):
        self.splitterTABD.SetHSplit(5000)
        self.splitterTABD.SetVSplit(5000)
    def OnButtonClickInicio(self, event):
        print("inicio")
        self.Refresh()
    def OnButtonClickConfiguracion(self, event):
        print("confi")
        self.Refresh()
    def OnButtonClickGuardar(self, event):
        print("guardar")
        self.Refresh()
    def OnButtonClickPuntos(self, event):
        print("puntosmon")
        self.Refresh()
    def OnClickThetaPanel(self, e):
        print("Clic ThetaPanel")


    def OnClickThetaPanel(self, e):
        self.splitterTABD.SetHSplit(10000)
        self.splitterTABD.SetVSplit(10000)
        self.thetaPanel.GetMinimizarButton().on_clicked(self.OnButtonClicMinimizar)
    def OnClickAlphaPanel(self, e):
        self.splitterTABD.SetHSplit(0)
        self.splitterTABD.SetVSplit(10000)
        self.alphaPanel.GetMinimizarButton().on_clicked(self.OnButtonClicMinimizar)
    def OnClickBetaPanel(self, e):
        self.splitterTABD.SetHSplit(10000)
        self.splitterTABD.SetVSplit(0)
        self.betaPanel.GetMinimizarButton().on_clicked(self.OnButtonClicMinimizar)
    def OnClickDeltaPanel(self, e):
        self.splitterTABD.SetHSplit(0)
        self.splitterTABD.SetVSplit(0)
        self.deltaPanel.GetMinimizarButton().on_clicked(self.OnButtonClicMinimizar)

  





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