'''
Created on Apr 16, 2019

@author: admin
'''
def sum(a,b): #void function
    print("sum of ",a," and ", b, " is - ",a+b)
    
k = sum(34,22)
print("return of sum - ",k)

print("=======================")
def sumwithreturn(a,b,c):  #non-void function
    sum = a+b+c
    print("I am done")
    return sum   


s = sumwithreturn(33, 32, 21)
print("Sum of three number is - ",s)

print(sumwithreturn(55, 33, 22))

print(sumwithreturn(33, 22, 11)>110)