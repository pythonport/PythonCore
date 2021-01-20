'''
Created on Apr 25, 2019
Program to demonstrate the use of WriteLines()
@author: admin
'''
fin = open("studentsMarks.txt",'a+')
lst = []
for a in range(5):
    sname = input("Studnets name - ")
    smarks = input("Students marks - ")
    sdata = sname+ ' achived - '+smarks+'\n'
    lst.append(sdata)
print(lst)
fin.writelines(lst)
fin.flush()
print("====== Added datas are ======")
fin.seek(0)
print(fin.read())
fin.close()