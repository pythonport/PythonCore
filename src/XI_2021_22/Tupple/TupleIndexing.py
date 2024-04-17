'''
Created on Feb 18, 2022

@author: admin
'''
tpl = (4, 3, 4, 5, 6, 2, 3)

print(tpl[3])
print(tpl[-4])
print(tpl[-2:6])
print(tpl[:5])
print(tpl[:])
print(tpl[::2])
print('length of tuple', len(tpl))
print("15 in tpl - ", 15 in tpl)
print("15 in tpl - ", 15 not in tpl)
print("5 in tpl - ", 5 in tpl)

t1 = (45,55)
print(tpl+t1+tpl) #concatenation
print(t1*3) #replication


