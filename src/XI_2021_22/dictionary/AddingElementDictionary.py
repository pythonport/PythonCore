'''
Created on Mar 8, 2022

@author: admin
'''
d = {'name': 'Rahul', 'salary': 188543}
d['location']='Bokaro'
print(d)

if 'subject' in d :
    del d['subject']
else :
    print("Subject key is not part of dictionary")
print(d)