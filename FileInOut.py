#Esta clase se encarga de leer y guardar datos en el archivo
import csv
class FileInOut():
    def __init__(self):
        global file_location_Input
        file_location_Input = "./InData.csv"

	#Este metodo lee el archivo
    def ReadData(self):
        file = open(file_location_Input, newline='')
        spamreader = csv.reader(file, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


