#Esta clase creea paneles  o pantallas que se visualizan con botones, graficas, imagenes, etc...
import wx
import os
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure 

from FileInOut import FileInOut

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

file = FileInOut()
file.ReadData()
class BraiNerdPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour(wx.Colour(121,255,255,0))

    #Mostrar el panel que contiene al menú.
    def ShowMenuPanel(self):
        self.SetBackgroundColour(wx.Colour(121,255,255,0))
        self.inicio = wx.Button(self, label='Inicio',pos=(200,90), size=(140, 25))
        self.configuracion = wx.Button(self, label='Configuracion',pos=(350, 90), size=(140, 25))
        self.guardar = wx.Button(self, label='Guardar',pos=(500,90), size=(140, 25))
        self.puntosMon = wx.Button(self, label='Puntos de Monitoreo',pos=(650, 90), size=(140, 25))
        bitmap = wx.Bitmap('LogoB.jpg')
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(80, 80, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        control = wx.StaticBitmap(self, -1, result)
        control.SetPosition((450, 0))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickInicio, self.inicio) 
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickConfiguracion, self.configuracion) 
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickGuardar, self.guardar) 
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickPuntos, self.puntosMon)

    def OnButtonClickInicio(self, event):
        self.SetBackgroundColour('Yellow')
        self.Refresh()
    
    def OnButtonClickConfiguracion(self, event):
        self.SetBackgroundColour('Blue')
        self.Refresh()
  
    def OnButtonClickGuardar(self, event):
        self.SetBackgroundColour('Red')
        self.Refresh()
  
    def OnButtonClickPuntos(self, event):
        self.SetBackgroundColour('Pink')
        self.Refresh()


    #Mostrar el panel que contiene al primer cuadrante con la grafica que representa las ondas Theta.
    def ShowThetaPanel(self):
        global N, r, theta, area, colors
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
    #Mostrar el panel que contiene al segundo cuadrante con la grafica que representa las ondas Alpha.
    def ShowAlphaPanel(self):
        self.SetBackgroundColour(wx.Colour(121,255,255,0))

    #Mostrar el panel que contiene al tercer cuadrante con la grafica que representa las ondas Beta.
    def ShowBetaPanel(self):
        self.SetBackgroundColour(wx.Colour(121,255,255,0))


    #Mostrar el panel que contiene al cuarto cuadrante con la grafica que representa las ondas Delta.
    def ShowDeltaPanel(self):
        self.SetBackgroundColour(wx.Colour(121,255,255,0))
       