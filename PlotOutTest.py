import csv
filelist = input("Enter .txt file containing filenames\n")
 
fileNames = []

fields = open(filelist, 'r')
with fields:
	files = csv.reader(fields)
	for row in files:
		fileNames.append(row[0][:-1])
		
print (fileNames)