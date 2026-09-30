'''
Created on Aug 18, 2026
Program to flush the data and read at same time.
@author: admin
'''
file = open('studentdata.txt','w+')
file.write('harish\n')
file.write('girish\n')
file.write('manish\n')
file.flush()

file.write('nitin\n')
file.write('binit\n')
file.write('bimal\n')
file.flush()
file.seek(0)
print(file.read())
file.close()