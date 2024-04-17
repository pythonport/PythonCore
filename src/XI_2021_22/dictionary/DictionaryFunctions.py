'''
Created on Mar 9, 2022

@author: admin
'''
dc = {'v1':'a', 'v2':'e', 'v3':'i', 'v4':'o', 'v5':'u'}
print("Length of dictionary - ",len(dc))

print("Value of V2 - ",dc.get('v8',"Key Not found"));

print("Dictionary items - ", dc.items())
print("Dictionary Keys - ", dc.keys())
print("Dictionary Values - ", dc.values())