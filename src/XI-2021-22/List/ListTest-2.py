'''
Created on Mar 8, 2022
Shift all zero element to last of list.
@author: admin
'''
#lst = [0, 45, 66, 0, 3, 4, 0, 0, 23, 45]
'''
lstzero = []
for i in lst :
    if(i == 0):
        lstzero.append(i)

for i in lst :
    if(i==0) :
        lst.remove(i)       

lst.extend(lstzero)        
print(lst)
#print(lstzero)
'''
lst = [0, 45, 66, 0, 3, 4, 0, 0, 23, 45]
n= len(lst)
count = 0 
for i in range(n):
    if lst[i]!=0:
        lst[count]=lst[i]
    count+=1
    
while(count<n) :
    lst[count]=0
    count+=1
print("list after passing all zero to end is - ")
print(lst)
    
