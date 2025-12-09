'''
Created on Dec 2, 2025

@author: admin
'''

Company  =[]

def PUSH_EMP(obj) :
    if(obj[1][-1]=='a' and obj[3] >50000) :
        emp = [obj[0], obj[1], obj[3]]
        Company.append(emp)

def POP_EMP() :
    while Company :
        print(Company.pop())

def PEEK_EMP() :
    print(Company[-1])