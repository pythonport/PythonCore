'''
Created on Jan 8, 2020

@author: admin
'''
import json

text = "Hello I am using Python and learing python programming I am using using hello"
words = text.split()

d= {}
for key in words :
    if key not in d :
        count  = words.count(key)
        d[key] = count

print("Frequency of elements are - ")
print(json.dumps(d, indent=4))