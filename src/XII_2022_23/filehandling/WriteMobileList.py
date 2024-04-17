'''
Created on Sep 14, 2022

@author: admin
'''
fout = open('friendMobile1.txt','w')
lst = []
for i in range(5):
    name = input("Name - ")
    phone = input('Phone - ')
    str  = name+' -> '+phone+'\n'
    lst.append(str)
print(lst)
fout.writelines(lst)
fout.close()
print('Writing done')