import csv
fh = open('empdata.csv', 'w', newline='')
mycsv = csv.writer(fh)

header = ['empid', 'ename', 'salary']
mycsv.writerow(header)

emp1 = [101,'abc',7845]
emp2 = [102,'xyz',9845]
emp3 = [103,'akk',8845]
mycsv.writerow(emp1)
mycsv.writerow(emp2)
mycsv.writerow(emp3)

print('done')
fh.close()