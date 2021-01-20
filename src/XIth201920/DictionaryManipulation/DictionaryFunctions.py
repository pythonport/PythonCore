'''
Created on Jan 8, 2020

@author: admin
'''
info = {'name': 'ravi ranjan', 'age': 18, 'classs': 'XII'}

sq = info.items()
print(sq)

for key,val in sq :
    print(key,"==>", val)