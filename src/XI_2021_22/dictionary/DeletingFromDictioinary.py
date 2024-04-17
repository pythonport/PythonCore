'''
Created on Mar 14, 2022

@author: admin
'''
d = {1:33, 2:44, 5:44, 6:76, 2:32}

print('Before deleting element - ',d)
'''
del d[5]
print('After deleting element - ',d)
del d
print('Deleting the dictionary - ',d)
'''
keynum = 8
val = 0
if (keynum in d) :
    val = d.pop(keynum)
else :
    print("No key found")

print('After popping', keynum,' key the element  - ',d)
print('Popped element  - ',val)