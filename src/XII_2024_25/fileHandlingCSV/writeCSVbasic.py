'''
Created on Oct 5, 2024

@author: admin
'''
import csv
file = open('sturesult.csv', 'a', newline='')
s1 = [11, 'Jatin Prasad', 57]
s2 = [13, 'Pradip Prasad', 51]

csvwriter = csv.writer(file)

csvwriter.writerow(s1)
csvwriter.writerow(s2)
print('done')
