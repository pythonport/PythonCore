'''
Created on Jul 19, 2019

@author: admin
'''
fin = open('xyzToWrote.txt','w')
lst = []
str1 = "Welcome to\n"
str2 = "jnv bokaro\n"
str3 = "Class XII Science\n"
str4 = "Python programming"

lst.append(str1)
lst.append(str2)
lst.append(str3)
lst.append(str4)

fin.writelines(lst)
fin.close()
print("Writting is done")

fout  = open('xyzToWrote.txt','r')
while True :
    fout.seek(0)    
    print("Current cursor position - ",fout.tell())
    str = fout.read()
    print(str)
    print("Current cursor position - ",fout.tell())
    print("--"*15)
    flag = input("Do you want to read more[0/1] - ")
    flag = False if flag=='0' else True
    if flag==False:
        print('Bye...')
        break
fout.close