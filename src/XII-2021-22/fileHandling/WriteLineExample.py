'''
Created on Sep 20, 2021

@author: admin
'''
fout = open('student.txt', 'a+')
for i in range(1):
    sname = input("Enter students name - ")
    fout.write(sname + '\n')
print("ok")
fout.flush()
fout.seek(0)  # taking the file pinter to beginning
sdata = fout.read()
print(sdata)
for i in range(10, 12, -1) :
    print('hello')
fout.close()
