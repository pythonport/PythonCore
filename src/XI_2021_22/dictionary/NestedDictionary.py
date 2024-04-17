'''
Created on Mar 8, 2022

@author: admin
'''
import json
marks = {'roll':1, 'name':'Abhay', 'smarks':{'che':99, 'phy':98, 'eng':87, 'maths':95, 'cs':100}}
print('Roll-', marks['roll'])
print('Name -', marks['name'])
print("English marks -", marks['smarks']['eng'])

jdata = json.dumps(marks, indent=5)
print(jdata)
