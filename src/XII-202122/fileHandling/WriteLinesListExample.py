'''
Created on Sep 20, 2021

@author: admin
'''
fout  = open('student-12.txt','w')
lst = []
for i in range(5):
    sname = input("Enter students name - ")
    lst.append(sname+'\n')

print("Name in list format - ",lst)
fout.writelines(lst)
print("ok")
fout.close()