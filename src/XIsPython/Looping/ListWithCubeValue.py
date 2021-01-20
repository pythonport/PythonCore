'''
Created on Dec 18, 2018

@author: Rajesh Kumar Jha
'''

lst = [2,3,4,5,6]
print(lst)
for i in range(len(lst)):
    lst[i]=lst[i]**3
print(lst)


A=[2,4,6,8,10]
L=len(A)
S=0
for I in range(1,L,2):
    S+=A[I]
print ('Sum=',S)
