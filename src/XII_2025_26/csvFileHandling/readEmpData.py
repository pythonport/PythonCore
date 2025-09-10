import csv
fh = open('empdata.csv', 'r', newline='')
mycsv = csv.reader(fh)

for row in mycsv :
    print(row)