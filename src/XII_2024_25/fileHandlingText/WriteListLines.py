'''
Created on Aug 30, 2024

@author: admin
'''
fout = open('studentmarks1.txt','w')
stumarks1 = 'sumit,400\n'
stumarks2 = 'faizan,785\n'
stumarks3 = 'mrityunjay,658\n'
stumarks4 = 'arya,258\n'
stumarks5 = 'anu,745'

stulist = []
stulist.append(stumarks1)
stulist.append(stumarks2)
stulist.append(stumarks3)
stulist.append(stumarks4)
stulist.append(stumarks5)

fout.writelines(stulist)
print(stulist)
fout.close()
print("writing done")

fout1 = open('studentmarks1.txt','r')
str = fout1.read()
print(str)
