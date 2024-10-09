'''
Created on Aug 31, 2024

@author: admin
'''
fout = open('feelist.txt', 'a')
feelist = []
ans = 'y'
while ans == 'y':
    sname = input('Enter name - ')
    fee = input('Fee - ')
    studata = sname + '->' + fee
    feelist.append(studata)
    ans = input('Do you want to continue [y/n] - ')

print(feelist)
fout.writelines(feelist)
print('Data saved successfully')
    
