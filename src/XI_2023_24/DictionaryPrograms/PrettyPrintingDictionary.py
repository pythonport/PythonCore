'''
Created on Jan 27, 2024

@author: Admin
'''
import json
employees = {'patna':{1:50000, 2:525252, 3:65656, 4:524141}, 'ranchi':{1:50000, 2:525252, 3:65656, 4:524141}, 'kolkata':{1:50000, 2:525252, 3:65656, 4:524141}, 'bhuwneshwar':{1:50000, 2:525252, 3:65656, 4:524141}, 'dhanbad':{1:50000, 2:525252, 3:65656, 4:524141}}

print(json.dumps(employees, indent=2))
