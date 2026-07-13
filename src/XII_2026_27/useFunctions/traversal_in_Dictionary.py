'''
Created on Apr 13, 2026

@author: admin
'''

#TRAVERSING in DICTIONARY.
dc1 = {'mon': 15, 'tue': 16, 'wed': 12, 'thu': 18, 'fri': 14, 'sat': 17, 'sun': 12}
for key in dc1 :
    print(key,'->',dc1[key])

print('----')  
#method-2 of item iteration in dictionary
for key, value in dc1.items() :
    print(key,'->',value)