import FileIn
from BraiNerdPanel import BraiNerdPanel
import wx
import wx.lib.agw.fourwaysplitter as fws

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


if __name__ == "__main__":
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()