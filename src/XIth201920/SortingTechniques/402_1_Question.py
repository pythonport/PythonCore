'''
Created on Jan 18, 2020

@author: admin
'''
d = {45:'hari',23:'laxmi',99:'purnima',54:'josnam'}

a = list(d.keys())
b = list(d.values())
print("unsorted votes - ",a)
a.sort(reverse=True)
print("Sorted votes - ",a)
print(b)

print('*'*25)
for i in range(len(a)):
    print(d.get(a[i])," Received - ",a[i])
print('*'*25)

print("Done")