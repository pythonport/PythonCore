'''
Created on Oct 16, 2023

@author: Admin
'''
def Diff(N1,N2):
    if N1>N2:
        return N1-N2
    else:
        return N2-N1
NUM= [10,23,14,54,32]
for CNT in range (4,0,-1):
    A=NUM[CNT]
    B=NUM[CNT-1]
    print(Diff(A,B),'#', end=' ')