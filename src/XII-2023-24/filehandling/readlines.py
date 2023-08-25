'''
Created on Jul 24, 2023

@author: ACER
'''
fout = open('12science.txt', 'r')
sdata = fout.readlines()
print(sdata)
print('no of element ',len(sdata))
print('Third element is ',sdata[2])
fout.close()