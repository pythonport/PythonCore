'''
Created on Aug 18, 2025

@author: admin
'''
fh = open('examstory.txt')
st = fh.read()
listword = st.split()
vcount = 0
vlist = ['a','e','i','o','u','A','E','I','O','U']
for word in listword :
    if word[0] in vlist :
        vcount+=1

print('Total word starts from vowel is - ',vcount)