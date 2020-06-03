#Este es el main del proyecto
from BraiNerdPanel import BraiNerdPanel
from Electrodos import Electrodos
import wx
import wx.lib.agw.fourwaysplitter as fws
from numpy import arange, sin, pi

from FileInOut import FileInOut

#Main manda llamar todos los demas modulos de python para que sean visibles y anadidos al procesamiento necesario para el correcto funcionamiento del programa.
class Main(wx.Frame):
    def __init__(self):
        

        self.file = FileInOut()


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
        self.thetaPanel.ShowGraphPanel(self.electrodos.GetElectrodeInfo(),"Theta Graph")
        self.alphaPanel.ShowGraphPanel(self.electrodos.GetElectrodeInfo(), "Alpha Graph")
        self.betaPanel.ShowGraphPanel(self.electrodos.GetElectrodeInfo(), "Beta Graph")
        self.deltaPanel.ShowGraphPanel(self.electrodos.GetElectrodeInfo(), "Delta Graph")

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.TimeInterval, self.timer)
        self.timer.Start(6)

        self.Bind(wx.EVT_BUTTON, self.OnButtonClickInicio, self.menuPanel.InicioButton()) 
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickAbrir, self.menuPanel.AbrirButton()) 
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

    #interaccion con todos los botones de menu y las 'X' para los cuadrantes
    def OnButtonClicMinimizar(self, event):
        self.splitterTABD.SetHSplit(5000)
        self.splitterTABD.SetVSplit(5000)
    def OnButtonClickInicio(self, event):
        self.file.PrintData()
        self.Refresh()
    def OnButtonClickAbrir(self, event):
        self.file.OnOpen()
        self.Refresh()

    def OnButtonClickGuardar(self, event):
        self.Refresh()
    def OnButtonClickPuntos(self, event):
        self.Refresh()


    #se encarga de expandir cada cuadrante de visualizacion
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


    #ejecuciones que suceden en el intervalo de actualizacion del programa
    def TimeInterval(self, event):
        self.menuPanel.UpdateMenu()
        self.file.ReadData()
        if(self.file.SelectedFile()==True):
            self.thetaPanel.UpdateValues(self.file.GetThetaData())
            self.alphaPanel.UpdateValues(self.file.GetAlphaData())
            self.betaPanel.UpdateValues(self.file.GetBetaData())
            self.deltaPanel.UpdateValues(self.file.GetDeltaData())
            """
            print (self.file.GetThetaData())
            print (self.file.GetAlphaData())
            print (self.file.GetBetaData())
            print (self.file.GetDeltaData())
            """
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