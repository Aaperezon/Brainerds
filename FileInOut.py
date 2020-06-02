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
        self.row = []
	#Este metodo lee el archivo
    def ReadData(self):
        try:
            fileL = open(self.file_location_Input,'r')
            reader = csv.reader(fileL)
            row=list(reader)
            row = row[self.rowCount]
            newList = []
            a=1
            for i in range (0,len(row)/4):
                newList.append(row[a:a+4])
                a+=4
            zip(*newList)
            self.row = zip(*newList)
            self.rowCount+=1
        except:
            self.file_location_Input = ""

    def GetThetaData(self):
        return self.row[0]
    def GetAlphaData(self):
        return self.row[1]
    def GetBetaData(self):
        return self.row[2]
    def GetDeltaData(self):
        return self.row[3]

    
    def OnOpen(self):
        self.file_location_Input = ""
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

    def PrintData(self):
        
        data = [0.125, 0.128, 0.122, 0.028, 5.052, 8.248] #Los datos estan aqui

        with open('OutData.csv', mode = 'w') as csv_file:
            dataWriter = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            dataWriter.writerow(data)       #Estos datos son guardados

