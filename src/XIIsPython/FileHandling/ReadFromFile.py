'''
Created on Apr 27, 2019
Program to read data from text file using file
object
@author: admin@hostingraja.in
'''
fout = open("addr.txt", 'r') #open text file in read mode
a = fout.read() #read whole file byte by byte
print(a)        #print bytes already store in a
print('*'*30)
print("is file connection closed - ",fout.closed) #check connection
fout.close() #close the connection with file
print("is file connection closed - ",fout.closed)

print("test close")