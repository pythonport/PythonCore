'''
Created on Sep 2, 2020
Nested list comprehensive
@author: admin
'''

# lst = [(x,y) for x in range(5) for y in range(5)]
lst = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 0]
print(lst)

l1 = []
for x in range(5) :
    if x % 2 == 0 :
        for y in range(5) :
            if y % 2 == 0 :
                val = (x, y)
                l1.append(val)
print(l1)
