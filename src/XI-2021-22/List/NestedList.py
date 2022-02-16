'''
Created on Feb 12, 2022

@author: admin
'''
la = [22, 11]
lb = [33, 11]
lc = [11, 44, lb]
lx = [11, la, lc, 15]
print('la - ', la)
print('lb - ', lb)
print('lc - ', lc)
print('lx - ', lx)

print(lx[1][0])
print(lx[2][1])
print(lx[2][2][0])