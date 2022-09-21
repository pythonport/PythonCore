'''
Created on Sep 14, 2022

@author: admin
'''
fout = open('address.txt','r+')
str1 = fout.read()
print(str1)
str = 'jnv bokaro, pin-829123'
#str = 'jnv bokaro\npost-tenughat rb\nbokaro jharkhand\npin-829123'
fout.write(str)
fout.close()
print("Writing is done")