'''
Created on Aug 6, 2026
Program to store 5 friends name and phone in file called contacts.dat
@author: admin
'''
#fout = open('contacts.dat','a')
fout = open(r'D:\PythonEclipsePrograms\PythonCore\\src\XII_2026_27\fileHandling\contacts.dat','a')

name = input('Name - ')
phone = input('Phone - ')
contact = name+' - '+phone+'\n'
fout.write(contact)
fout.close()
print('done')

fout = open('contacts.dat','r')
print(fout.read())