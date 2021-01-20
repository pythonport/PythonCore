'''
Created on Dec 27, 2019

@author: admin
'''
s = 'python'
t = tuple(s)
length = len(t)
for a in t :
    print(a)

print('===='*4)    
for a in range(len(t)) :
    print('At index ',a,'And ',(a-length),' value is - ',t[a])

print('Thank you')