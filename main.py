import wx
import os
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure 
import wx.lib.agw.fourwaysplitter as fws

import FileIn

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class MenuPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)  
        self.SetBackgroundColour(wx.Colour(121,255,255,0))
        wx.Button(self, label='Inicio',pos=(200, 90), size=(140, 25))
        wx.Button(self, label='Configuracion',pos=(350, 90), size=(140, 25))
        wx.Button(self, label='Guardar',pos=(500,90), size=(140, 25))
        wx.Button(self, label='Puntos de Monitoreo',pos=(650, 90), size=(140, 25))
        pic = wx.Bitmap('Prueba.png', wx.BITMAP_TYPE_ANY)
        wx.BitmapButton(self, -1, pic, pos=(450,0),size=(80,80))



class ThetaPanel(wx.Panel):
    def __init__(self,parent):
        global N, r, theta, area, colors
        wx.Panel.__init__(self,parent)
        N = 11
        r = 2 * np.random.rand(N)
        theta = 2 * np.pi * np.random.rand(N)
        area = 200 * r**2
        colors = theta
        print (self.GetMinHeight) , "  ", (self.GetMinWidth)
        self.fig = Figure(figsize=[1,3.2])
        self.ax = self.fig.add_subplot(111, projection='polar') #puedo probar con ',facecolor='black'
        self.canvas = FigureCanvas(self, -1, self.fig)
        self.sizer  = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        pic = plt.imread('Prueba.png')
        ax_image = self.fig.add_axes([0,0,1,1], label="ax image")
        ax_image.imshow(pic, alpha=.5)
        ax_image.axis('off')  # don't show the axes ticks/lines/etc. associated with the image

        self.ax.scatter(theta-300, r, c=colors, s=area, cmap='hsv', alpha=0.75)

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
        splitter.SetMinimumPaneSize(120)


if __name__ == "__main__":
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()