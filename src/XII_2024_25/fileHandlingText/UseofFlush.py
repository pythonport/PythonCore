'''
Created on Aug 31, 2024

@author: admin
'''
fout = open('dueslist.txt', 'a')
ans = 'y'
while ans == 'y':
    sname = input('Enter name - ')
    fee = input('Fee - ')
    studata = sname + '->' + fee+'\n'
    ans = input('Do you want to continue [y/n] - ')
    fout.write(studata)
    fout.flush()

print('Data saved successfully')
fout.close()