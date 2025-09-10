'''
Created on Aug 28, 2025
Program to store employee data in csv file format
@author: admin
'''
import csv
fh = open('employeedata.csv','w', newline='')
jnvwriter = csv.writer(fh)
empheader = ['ecode','ename','salary']
jnvwriter.writerow(empheader)

em1 = [452,'amit',898956]
em2 = [453,'anita',898950]
em3 = [454,'jatin',898951]
em4 = [455,'kamat',898960]
jnvwriter.writerow(em1)
jnvwriter.writerow(em2)
jnvwriter.writerow(em3)
jnvwriter.writerow(em4)
print('done')
fh.close()