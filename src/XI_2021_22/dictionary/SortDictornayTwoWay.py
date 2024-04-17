'''
Created on Mar 15, 2022

@author: admin
'''
stu = {41:'Neha', 12:'Saima', 32:'Anvit', 24:'Ana', 15:'Shaji'}
sortedKeys1 = sorted(stu)
print(sortedKeys1)
sortedkeys2= sorted(stu.keys())
print('Sorted Keys are - ',sortedkeys2)

sortedvalues = sorted(stu.values())
print('Sorted Values are - ',sortedvalues)

sorteditems = sorted(stu.items())
print('Sorted Items are - ',sorteditems)