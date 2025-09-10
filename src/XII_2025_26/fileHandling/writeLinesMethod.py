'''
Created on Aug 1, 2025

@author: admin
'''
file = open('friendlist.txt','w')
flist = ['abc\n','juj\n','abb\n','acb\n','xzy\n','zzy\n','aby\n','abz\n']
file.writelines(flist)
file.close()
print('done')