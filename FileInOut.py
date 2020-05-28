#Esta clase se encarga de leer y guardar datos en el archivo
import csv
from csv import reader
import wx
class FileInOut():
    def __init__(self):
        self.file_location_Input = ""

	#Este metodo lee el archivo
    def ReadData(self,fileName):
        file = open(fileName, 'r')
        csv_reader = reader(file)
        # Iterate over each row after the header in the csv
        for row in csv_reader:
        # row variable is a list that represents a row in csv
            print(row)


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
        self.ReadData(self.file_location_Input)


