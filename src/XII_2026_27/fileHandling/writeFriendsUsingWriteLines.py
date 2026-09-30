'''
Created on Aug 7, 2026

@author: admin
'''
fout = open('contacts.dat','w')
lstfriends = []
for i in range(5):
    name = input('Name - ')
    phone = input('Phone - ')
    contact = name+' - '+phone+'\n'
    lstfriends.append(contact)
print(lstfriends)
fout.writelines(lstfriends)
fout.close()
print('done')