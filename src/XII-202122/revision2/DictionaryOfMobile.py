'''
Created on Jul 15, 2021

@author: admin
'''
contacts = {'afjal' : 9988554433, 'amit':343344445, 'rajkumar':887766773, 'ravi':45333334}
print(contacts)
print(contacts.keys())
print(contacts.values())

for name in contacts :
    #print('Mobile no of {0} is {1}'.format(name, contacts[name]))
    print('Mobile no of',name,' is ',contacts[name])
