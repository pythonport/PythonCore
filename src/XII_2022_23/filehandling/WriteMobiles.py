'''
Created on Sep 14, 2022
Take input from user (name and mobile number) of five friends
and store in file called friendMobile.txt file.
@author: admin
'''

fout = open('friendMobile.txt','w')
for i in range(5):
    name = input("Name - ")
    phone = input('Phone - ')
    str  = name+' -> '+phone+'\n'
    fout.write(str)
fout.close()
print('Writing done')