'''
Created on Sep 14, 2022

@author: admin
'''
fout = open('poem.txt','r')
poemText = fout.readlines()
print(poemText)
print('Number of lines in poem is - ',len(poemText))
fout.close()