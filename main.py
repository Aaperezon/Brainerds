#Este es el main del proyecto
from BraiNerdPanel import BraiNerdPanel
import wx
import wx.lib.agw.fourwaysplitter as fws
#Main manda llamar todos los demás modulos de python para que sean visibles y añadidos al procesamiento necesario para el correcto funcionamiento del programa.
class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = "Brainerds",size = (1000,800))
        splitter = wx.SplitterWindow(self)
        splitterTABD = fws.FourWaySplitter(splitter)

        thetaPanel = BraiNerdPanel(splitterTABD)
        alphaPanel = BraiNerdPanel(splitterTABD)
        betaPanel = BraiNerdPanel(splitterTABD)
        deltaPanel = BraiNerdPanel(splitterTABD)

        menuPanel = BraiNerdPanel(splitter)
        splitter.SplitHorizontally(menuPanel, splitterTABD)

        splitterTABD.AppendWindow(thetaPanel)
        splitterTABD.AppendWindow(alphaPanel)
        splitterTABD.AppendWindow(betaPanel)
        splitterTABD.AppendWindow(deltaPanel)
        splitter.SetMinimumPaneSize(120)

        menuPanel.ShowMenuPanel()
        thetaPanel.ShowThetaPanel()
        alphaPanel.ShowAlphaPanel()
        betaPanel.ShowBetaPanel()
        deltaPanel.ShowDeltaPanel()

#Comprueba que éste archivo sea el main ejecutable para poder ejecutarlo
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