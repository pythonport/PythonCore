'''
Created on Jan 8, 2020

@author: admin
'''
import json

info = {"name":"ravi ranjan","age":18,"classs":"XII"}
phonsOfFriends = {'mohit':98784333,'sanjay':45553434,'praful':6776555,'joshna':64434241}

#print(info)

print(json.dumps(info, indent=2))
print(json.dumps(phonsOfFriends, indent=4))