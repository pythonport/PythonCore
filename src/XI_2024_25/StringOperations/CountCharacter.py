'''
Created on Jan 20, 2025

@author: admin
'''
str = 'Hello to you too much from too much'
chr = 'o'
print('count of o is - ',str.count(chr))

#=======================

chrcount = 0
for ch in str :
    if ch == chr :
        chrcount+=1
        
print('count of o using for loop is - ',chrcount)