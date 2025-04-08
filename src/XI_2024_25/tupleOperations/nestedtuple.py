'''
Created on Feb 18, 2025

@author: admin

from tabulate import tabulate

st=((101,"Aman",98),(102,"Geet",95),(103,"Sahil",87),(104,"Pawan",79))
#print("Roll_No"," Name"," Marks")
tbl = tabulate(st, headers=["Roll_No"," Name"," Marks"])
print(tbl)
'''

#iterating nested tuple using for loop
tpl = (('sahil', 12, 98.5),('kamal', 10, 88.5),('Lakhan', 9, 78.5))

for i in range(len(tpl)) :
    print('Name - ',tpl[i][0])
    print('Class - ',tpl[i][1])
    print('Marks - ',tpl[i][2])
    print('--------------------')
    