'''
Created on Aug 6, 2026
Program to store 5 friends name and phone in file called contacts.dat
@author: admin
'''
fout = open('contacts.dat','w')
for i in range(5):
    name = input('Name - ')
    phone = input('Phone - ')
    contact = name+' - '+phone+'\n'
    fout.write(contact)
fout.close()
print('done')