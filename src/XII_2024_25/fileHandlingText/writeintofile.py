'''
Created on Aug 30, 2024

@author: admin
'''
fout = open('studentmarks.txt','w')
stumarks1 = 'sumit,40\n'
stumarks2 = 'faizan,40\n'
stumarks3 = 'mrityunjay,40\n'
stumarks4 = 'arya,40\n'
stumarks5 = 'anu,40'

fout.write(stumarks1)
fout.write(stumarks2)
fout.write(stumarks3)
fout.write(stumarks4)
fout.write(stumarks5)
fout.close()
print("writing done")

fout1 = open('studentmarks.txt','r')
str = fout1.read()
print(str)