'''
Created on Sep 8, 2022

@author: admin
'''

#fout  = open('poem.txt')
#fout  = open('studentlist.txt')
#fout  = open('C:\\Users\\admin\\Desktop\\sturoll.txt')
jnvroll  = open(r'C:\Users\admin\Desktop\sturoll.txt')
print(id(jnvroll))
data = jnvroll.read()
print(data)
jnvroll.close()
print(id(jnvroll))
jnvroll.seek(0)
data1 = jnvroll.read()
print(data1)