'''
Created on Mar 28, 2019

@author: admin
'''
value = [15,16,17,18]
for val in value :
    for i in range(1,val%13):
        print(i, "* ", end="")
    print()