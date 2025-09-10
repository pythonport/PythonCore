'''
Created on Aug 4, 2025

@author: admin
'''
file = open('stumarks.txt','w+')
file.write('abhishek-40\n')
file.write('akash-42\n')
file.write('shubjeet-43\n')
file.write('nayan-43\n')
file.flush()
file.seek(0)
s = file.read()
print(s)