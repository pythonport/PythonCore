'''
Created on Aug 1, 2026

@author: admin
'''
str = "Hello I am at JNV dhanbad, studying computer science\n"
lang = 'Language-Python\n'
topic = 'File Handling\n'

file1 = open('mydata.txt','w')
file1.write(str)
file1.write(lang)
file1.write(topic)
file1.close()
print('done')