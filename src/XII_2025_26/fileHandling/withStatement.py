'''
Created on Aug 5, 2025
Code to use with statement to read and write data onto file.
@author: admin
'''
with open('friendlist.txt','w') as f :
    f.write('Fist line\n')
    f.write('Second line\n')
    f.write('Third line\n')
    f.write('Fourth line\n')

print('I am done')
with open('friendlist.txt','r') as fh :
    print(fh.read())