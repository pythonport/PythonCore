'''
Created on Mar 27, 2024
Count word in file
@author: Admin
'''

fout = open('wordcount.txt','r')
data = fout.read()
print(data)

words= data.split()
#print(words)
#print('Total words - ',len(words))

scount = 0
for word in words :
    if word[0] =='s' or word[0] =='S' :
        scount+=1

print('Total words starts with s - ',scount)