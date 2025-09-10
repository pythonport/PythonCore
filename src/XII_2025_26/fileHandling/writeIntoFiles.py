'''
Created on Jul 30, 2025

@author: admin
'''
file = open('studentlist.txt','w')
for i in range(5) :
    name = input('Student Name - ')
    file.write(name+'\n')
file.close()