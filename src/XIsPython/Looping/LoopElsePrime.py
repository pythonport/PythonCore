'''
Created on Dec 11, 2018
Python module for for loop
@author: Rajesh Kumar jha
'''

l = []
for i in range(1,11):
    l.append(i)

print(l)

for i in range(len(l)):
    l[i]=(l[i]**2)
  
print(l)

#===============================================================================
# for i in l :
#     print(i)
#     
# print("=============")
# 
# for i in range(len(l)) :
#     print(i)    
#===============================================================================