'''
Created on Sep 10, 2026

@author: admin
'''
import csv
fout = open('stumarks.csv','w', newline='')
jnvwriter = csv.writer(fout)

header = ['roll','name','marks']
jnvwriter.writerow(header)

stu1 = [1,'manish',92]
stu2 = [2,'abhay',93]
jnvwriter.writerow(stu1)
jnvwriter.writerow(stu2)

fout.close()
print('done')