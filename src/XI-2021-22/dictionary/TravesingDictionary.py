'''
Created on Mar 5, 2022

@author: admin
'''
dc = {'v1':'a', 'v2':'e', 'v3':'i', 'v4':'o', 'v5':'u'}

for a in dc :
    print(a," having value -  ",dc[a])
    
print(dc.keys())
print(type(dc.keys()))
print(dc.values())
print(type(dc.values()))