#Esta clase crea paneles  o pantallas que se visualizan con botones, graficas, imagenes, etc...
import wx
import wx.xrc as xrc
import os
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure 


import wx.lib.agw.buttonpanel as BP
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button
import  cStringIO



class BraiNerdPanel(wx.Panel):
   
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.r = 0
        self.theta = 0
        self.color = []
        
        
    #Mostrar el panel que contiene al menu
    def ShowMenuPanel(self):
        self.SetBackgroundColour(wx.Colour(121,255,255,0))
        self.inicio = wx.Button(self, label="Inicio",pos=(200,90), size=(140, 25))
        self.abrir = wx.Button(self, label='Abrir',pos=(350, 90), size=(140, 25))
        self.guardar = wx.Button(self, label='Guardar',pos=(500,90), size=(140, 25))
        self.puntosMon = wx.Button(self, label='Puntos de Monitoreo',pos=(650, 90), size=(140, 25))
        
        bitmap = wx.Bitmap('LogoB.jpg')
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(80, 80, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        self.control = wx.StaticBitmap(self, -1, result)
        self.control.SetPosition((450, 0))
       
   
    def InicioButton(self):
        return self.inicio
    def AbrirButton(self):
        return self.abrir
    def GuardarButton(self):
        return self.guardar
    def PuntosMonButton(self):
        return self.puntosMon
   

    def UpdateMenu(self):
        X,Y = self.GetSize()
        Y = Y-30
        if(X>=0):
            iniX = (X/2)-300
            abrirX = (X/2)-150
            guaX = (X/2)+10
            ptsMonX = (X/2)+160
            self.inicio.SetPosition(wx.Point(iniX,Y))
            self.abrir.SetPosition(wx.Point(abrirX,Y))
            self.guardar.SetPosition(wx.Point(guaX,Y))
            self.puntosMon.SetPosition(wx.Point(ptsMonX,Y))
            self.control.SetPosition(((X/2)-40, 0))
       
  

    def SetAngleElectrode(self, angle):
        self.theta = angle
    def SetRElectrode(self, r):
        self.r = r

    def GetAngleElectrode(self):
        return self.theta
    def GetRElectrode(self):
        return self.r

    def PutGraphIn(self):
        self.fig = Figure(figsize=[2,2]) #Grafica tamano
        self.ax = self.fig.add_subplot(111, projection='polar') #puedo probar con ',facecolor='black'
        self.canvas = FigureCanvas(self, 1, self.fig)
        self.sizer  = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.pic = plt.imread('Cerebro.png') #imagen de fondo del cerebro
        self.ax_image = self.fig.add_axes([.06,.1,.9,.8], label="ax image")
        self.ax_image.imshow(self.pic, alpha=.5)
        self.ax_image.axis('off')  # don't show the axes ticks/lines/etc. associated with the image
        self.ax.grid(False) # circulos internos de la grafica
        self.ax.set_yticklabels([]) # etiquetas de diagonar r
        self.ax.set_xticklabels([]) # etiquetas de circunferencia grados
        self.point = self.ax.scatter(self.GetAngleElectrode(),self.GetRElectrode(), c=np.zeros(32), s=(100), cmap='hsv', alpha=0) #dibuja la grafica

    def UpdateValues(self,dataIn):
        self.fig.canvas.draw()
        self.point.remove()
        for a in dataIn:
            a = float(a)
            if (a >= 0.0 and a <= 0.142858):
                self.color.append('blue')
            elif (a > 0.142858 and a <= 0.428572):
                self.color.append('cyan')
            elif (a > 0.428572 and a <= 0.571429):
                self.color.append('lightgreen')
            elif (a > 0.571429 and a <= 0.724285):
                self.color.append('yellow')
            elif (a > 0.724285 and a <= 0.867142):
                self.color.append('orange')
            elif (a > 0.867142):
                self.color.append('red')
        #print (self.color)
        self.point = self.ax.scatter(self.GetAngleElectrode(),self.GetRElectrode(), c=self.color, s=(100), cmap='hsv', alpha = 1) #dibuja la grafica
        self.color = []
        
    def GetCanvas(self):
        return self.canvas
    def GetPanel(self):
        return self
    #inicializa el boton 'X' de todos los cuadrantes
    def ShowMinimizarButton(self):
        self.minimizar = Button(self.fig.add_axes([.95,.95,.05,.05]),"X")
    #retorna la varibale del boton 'X' para otra clase que lo quiera controlar
    def GetMinimizarButton(self):
        return self.minimizar
    #Mostrar el panel que contiene el cuadrante con la grafica.
    def ShowGraphPanel(self,info,nameGraph):
        self.SetAngleElectrode(info[2])
        self.SetRElectrode(info[1])
        self.PutGraphIn()
        self.ax.set_title(nameGraph)