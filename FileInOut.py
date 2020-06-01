#Esta clase se encarga de leer y guardar datos en el archivo
import csv
from csv import reader
import wx
import pandas as pd
import string
class FileInOut():
    def __init__(self):
        self.file_location_Input = ""
        self.rowCount = 0
	#Este metodo lee el archivo
    def ReadData(self):
        df = pd.read_csv(self.file_location_Input, skiprows=self.rowCount,nrows=0)
        row = df.iloc[:,:]
        row = list(row)
        newList = []
        a=1
        for i in range (0,len(row)/4):
            newList.append(row[a:a+4])
            a+=4
        #print (newList)
        self.rowCount+=1
        return zip(*newList)
      
    
    def OnOpen(self):
        frame = wx.Frame(None, -1, 'win.py')
        frame.SetDimensions(0,0,200,50)

        # Create open file dialog
        openFileDialog = wx.FileDialog(frame, "Seleccion de archivo", "", "", 
            "Python files (*.csv)|*.csv", 
            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        self.file_location_Input = openFileDialog.GetPath()
        #print(openFileDialog.GetPath())
        openFileDialog.Destroy()
        #return self.ReadData(self.file_location_Input)
    def SelectedFile(self):
        if (self.file_location_Input == ""):
            return False
        else:
            return True

