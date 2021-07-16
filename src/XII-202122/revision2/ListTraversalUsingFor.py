'''
Created on Jul 8, 2021

@author: admin
'''

lst = [45, 23, 23, 67, 45, 44, 5, 2, 3, 4, 7]

print(lst[: :2])

for i in lst :
    print(i)
    
print('-----------')   
 
for i in range(len(lst)):
    print(i,' - ',lst[i])
