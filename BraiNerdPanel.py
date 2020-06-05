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
        self.SetBackgroundColour(wx.Colour(110,173,254,0))
        
        
    #Mostrar el panel que contiene al menu
    def ShowMenuPanel(self):
        self.inicio = wx.Button(self, label="Inicio",pos=(200,80), size=(140, 25))
        self.abrir = wx.Button(self, label='Abrir',pos=(350, 80), size=(140, 25))
        self.guardar = wx.Button(self, label='Guardar',pos=(500,80), size=(140, 25))
        self.puntosMon = wx.Button(self, label='Puntos de Monitoreo',pos=(650, 80), size=(140, 25))

        font = wx.Font(10, wx.SCRIPT, wx.NORMAL, wx.NORMAL, 0, "")
        self.inicio.SetFont(font)
        self.abrir.SetFont(font)
        self.guardar.SetFont(font)
        self.puntosMon.SetFont(font)

        bitmap = wx.Bitmap('./img_src/BrainNerds150x60.png')
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(150, 60, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        self.control = wx.StaticBitmap(self, -1, result)
        self.control.SetPosition((450, 10))

        self.textTime = wx.StaticText(self, -1, "Tiempo de lectura: 0 s.", pos=(20, 50))

   
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
        Y = Y-40
        if(X>=0):
            iniX = (X/2)-300
            abrirX = (X/2)-150
            guaX = (X/2)+10
            ptsMonX = (X/2)+160
            self.inicio.SetPosition(wx.Point(iniX,Y))
            self.abrir.SetPosition(wx.Point(abrirX,Y))
            self.guardar.SetPosition(wx.Point(guaX,Y))
            self.puntosMon.SetPosition(wx.Point(ptsMonX,Y))
            self.control.SetPosition(((X/2)-75, 10))
        
       
    def UpdateTime(self,time):
        a = "Tiempo de lectura: "+str(time)
        self.textTime.SetLabelText(a)
  

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
        self.pic = plt.imread('./img_src/Cerebro.png') #imagen de fondo del cerebro
        self.ax_image = self.fig.add_axes([.06,.1,.9,.8], label="ax image")
        self.ax_image.imshow(self.pic, alpha=.6)
        self.ax_image.axis('off')  # don't show the axes ticks/lines/etc. associated with the image

        self.pic2 = plt.imread('./img_src/paletaRGB.png') #imagen de la escala RGB
        self.ax_image2 = self.fig.add_axes([.5,.2,.8,.7], label="ax image")
        self.ax_image2.imshow(self.pic2, alpha=1)
        self.ax_image2.axis('off')  # don't show the axes ticks/lines/etc. associated with the image

        self.ax = self.fig.add_subplot(111, projection='polar') #puedo probar con ',facecolor='black'
        self.ax.patch.set_alpha(0)
        self.canvas = FigureCanvas(self, 1, self.fig)
        self.sizer  = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.ax.grid(False) # circulos internos de la grafica
        self.ax.set_yticklabels([]) # etiquetas de diagonar r
        self.ax.set_xticklabels([]) # etiquetas de circunferencia grados
        self.point = self.ax.scatter(self.GetAngleElectrode(),self.GetRElectrode(), c=np.zeros(32), s=(100), cmap='hsv', alpha=1) #dibuja la grafica

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
        titleFont = {'fontname':'Arial'}
        self.ax.set_title(nameGraph,fontsize= 15,**titleFont)