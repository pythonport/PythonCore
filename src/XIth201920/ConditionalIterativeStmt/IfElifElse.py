'''
Created on Sep 14, 2019

@author: admin
'''
num1 = int(input("Enter first number - "))
num2 = int(input("Enter second number - "))
op = input("Enter operator sign [+,-,*,/,%]- ")
result = 0

if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1/num2
elif op=='%':
    result=num1%num2
else :
    print("Invalid operator")

print(num1,op,num2,'=',result)