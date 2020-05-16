import wx
import os
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure 
import wx.lib.agw.fourwaysplitter as fws



class MenuPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        wx.Button(self,-1,"Button1")        
        self.SetBackgroundColour(wx.Colour(121,255,255,0))


class ThetaPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour(wx.Colour(121,255,255,0))
class AlfaPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour(wx.Colour(121,255,255,0))
class BetaPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour(wx.Colour(121,255,255,0))
class DeltaPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour(wx.Colour(121,255,255,0))

class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
   
       

class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = "Brainerds",size = (1000,800))
        splitter = wx.SplitterWindow(self)
        splitterTABD = fws.FourWaySplitter(splitter)

        thetaPanel = ThetaPanel(splitterTABD)
        alfaPanel = AlfaPanel(splitterTABD)
        betaPanel = BetaPanel(splitterTABD)
        deltaPanel = DeltaPanel(splitterTABD)

        menuPanel = MenuPanel(splitter)
        splitter.SplitHorizontally(menuPanel, splitterTABD)

        splitterTABD.AppendWindow(thetaPanel)
        splitterTABD.AppendWindow(alfaPanel)
        splitterTABD.AppendWindow(betaPanel)
        splitterTABD.AppendWindow(deltaPanel)
        splitter.SetMinimumPaneSize(100)

     



        

if __name__ == "__main__":
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()