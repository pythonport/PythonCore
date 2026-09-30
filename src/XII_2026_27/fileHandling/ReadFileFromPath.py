'''
Created on Aug 1, 2026

@author: admin
'''
#file1 = open('C:\\Users\\admin\\Desktop\\Shivalik_HouseData\\jnvdhanbad.txt','r')
file1 = open(r'C:\Users\admin\Desktop\Shivalik_HouseData\jnvdhanbad.txt','r')
data = file1.read(15)
print(data)
print('------')
data = file1.read(10)
print(data)

