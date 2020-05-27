#Esta clase se encarga de leer y guardar datos en el archivo
import csv
from csv import reader

class FileInOut():
    def __init__(self):
        self.file_location_Input = "./InData.csv"

	#Este metodo lee el archivo
    def ReadData(self):
        file = open(self.file_location_Input, 'r')
        csv_reader = reader(file)
        # Iterate over each row after the header in the csv
        for row in csv_reader:
        # row variable is a list that represents a row in csv
            print(row)




