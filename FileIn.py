import csv

with open('./InData.csv', newline='') as csvfile:
	file_location = "./InData.csv"
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print(', '.join(row))


