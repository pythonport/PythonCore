'''
Created on Jul 24, 2025

@author: admin
'''
file = open('dhanbad.txt','a+')
readData = file.read()
print(readData)
#strData = 'Nirsa, Gobindpur, Purbi Tundi, Paschmi Tundi, Baghmara, Topchanchi, Dhanbad'
strData = '\n JNV Dhanbad at Benagoria Nirsa'
file.write(strData)
print('Data Write successfully')
#file.seek(0)
#print(readData)
file.close()