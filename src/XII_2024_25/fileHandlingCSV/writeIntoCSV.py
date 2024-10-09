'''
Created on Oct 7, 2024

@author: admin
'''
import csv
bfile = open('books.csv', 'a', newline='')
bookwriter = csv.writer(bfile)

bookheader = ['slno',' book name','price']
book1 = [1 ,'Computer Science With Python', 550.00]


bookwriter.writerow(bookheader)
bookwriter.writerow(book1)
print('done')
bfile.close()