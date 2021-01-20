'''
Created on Feb 12, 2019

@author: admin
'''

for a in range(4,0,-1):
    val = ""
    start=4
    for b in range(a,0,-1) :
        val+=str(start)
        start-=1
    print(val)