import csv

#WOULD HAVE BEEN BETTER TO DO SOME KIND OF OS LISTDIR FOR TXT IN DIR
#BUT WHATEVER

dest = open('office.txt', 'r')
outputFile = open('office.csv', 'w')
outputWriter = csv.writer(outputFile)

for line in dest:
	
	row = line.split('|')
	row = row[1:-1]
		
	newRow = []
	
	for item in row:
		entry = item.rstrip().lstrip()
		newRow.append(entry)
	
	outputWriter.writerow(newRow)
	
dest.close()
outputFile.close()	
