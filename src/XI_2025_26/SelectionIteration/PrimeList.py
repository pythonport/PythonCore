'''
Created on Jan 8, 2026

@author: admin
'''
start = 50
end = 100
listPrime = []
for a in range(start, end+1) :
    lim = a//2+1
    for i in range(2, lim) :
        if a%i == 0 :
            break
    else :
        listPrime.append(a)

print('List of prime - ',listPrime)