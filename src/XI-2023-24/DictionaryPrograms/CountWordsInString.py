'''
Created on Jan 29, 2024

@author: Admin
'''
import json
mystring = 'This is python programm program is for every one  python is for everone'
dc = {}
words = mystring.split()
for key in words :
    if key not in dc :
        count = words.count(key)
        dc[key] = count

print(words)  
print(dc)
print(json.dumps(dc, indent=2))