'''
Created on Aug 16, 2024

@author: admin
'''
fout = open('E:\\UdayGiri-Boys-Photo\\StudentsName.txt')
#fout = open(r'E:\UdayGiri-Boys-Photo\StudentsName.txt')
str = fout.read()
print(str)
fout.close()
print('=========')
print(str)
if (fout.closed==True) :
    print('File closed')
else :
    str1 = fout.read()