'''
Created on Sep 13, 2024

@author: admin
'''
fout= open('poem.txt','rb')
print('current position - ',fout.tell())
fout.seek(150,0)
str =  fout.readline()
print(str)
print('current position - ',fout.tell())

print('---------------')
fout.seek(-50, 2)
str = fout.read()
print(str)
print('current position - ',fout.tell())
