'''
Created on Aug 17, 2019
Example of list Comprehension
@author: admin
'''

a = [(num if num < 5 else num * 2) for num in range(2, 9)]
print(a)

lst = [31, 15, 42, 12, 5, 39, 21, 61, 25]
mul3 = [i for i in lst if i % 3 == 0]
print(mul3)

res = []
for x in [10, 5, 2]:
    for y in[2, 3, 4]:
        res.append(x ** y)
    
print(res)

res1 = [x ** y for x in [10, 5, 2] for y in[2, 3, 4] ]
print(res1)


res2 = [(x,y) for x in range(5) if x%2==0 for y in range(5) if y%2==1]
print(res2)

res3 = []
for x in range(5):
    if x%2==0:
        for y in range(5):
            if y%2==1:
                res3.append((x,y))

print(res3)