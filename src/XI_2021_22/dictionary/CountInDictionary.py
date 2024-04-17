'''
Created on Mar 9, 2022

@author: admin
'''
import json
sentence = "This is python we class, python we today are studying dictionary is today"
word = sentence.split()
d = {}
for i in word :
    key = i
    if key not in d :
        count = word.count(key)
        d[key] = count

print("Counting frequencies in list - ", word)
print("Length of dictionary - ",len(d))
print("Length of sentence - ",len(sentence))
print(json.dumps(d, indent=2))        
