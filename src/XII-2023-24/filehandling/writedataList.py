'''
Created on Jul 26, 2023

@author: acer
'''
fout = open('stulist.txt','w')
slist = ['binay\n','prince\n','prem\n',
         'niharika\n','punam\n','kumkum']

slist1 = ['binay\t','prince\t','prem\t',
         'niharika\t','punam\t','kumkum']

fout.writelines(slist1)
fout.close()
print('OK Done')