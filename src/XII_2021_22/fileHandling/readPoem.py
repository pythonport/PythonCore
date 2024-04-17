'''
Write a program to display the size of file in bytes.
'''

fout = open('poem.txt','a+')
print('Current Position - ',fout.tell())
str1 = fout.read(20)
print(str1)
fout.seek(0)
print('Current Position - ',fout.tell())
print('----------')
str1 = fout.read(20)
print(str1)
print('Current Position - ',fout.tell())
fout.seek(100)
str1 = fout.read(50)
print(str1)
print('Current Position - ',fout.tell())