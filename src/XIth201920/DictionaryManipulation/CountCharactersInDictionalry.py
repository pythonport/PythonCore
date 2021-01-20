'''
Created on Jan 8, 2020

@author: admin
'''
import json

text = "Hello I am using Python and learing python programming I am using using hello"

d= {}
for key in text :
    if key not in d :
        count  = text.count(key)
        d[key] = count

print("Frequency of elements are - ")
print(json.dumps(d, indent=4))

print('*****************')
word = "hello python"
for c in word:
    print(c)