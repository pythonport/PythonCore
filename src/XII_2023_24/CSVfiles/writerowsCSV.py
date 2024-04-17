'''
Created on Sep 11, 2023

@author: Admin
'''
import csv
file = open('mobiles.csv','a', newline='')
mobwriter = csv.writer(file)
'''
mobilelist = []
for i in range(5):
    name = input('Enter name - ')
    mobile = input('Enter mobile number - ')
    row =[]
    row.append(name)
    row.append(mobile)
    mobilelist.append(row)
'''
    
#print(mobilelist)
header = ['name','mobile']
mobwriter.writerow(header)
mobilelist = [['abc', '8855'], ['ncs', '5522'], ['ysss', '8855'], ['tere', '87844'], ['tyre', '6655']]
mobwriter.writerows(mobilelist)
print('done')
file.close()