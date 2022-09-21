'''
Created on Jul 30, 2021

@author: admin
'''


# void function
def sayHello(name):
    print("Hello to you - ", name)


sayHello('Ravi Ranjan')
sayHello('Simran')

# non-void function
def sayHi(nm):
    greet = "Hello to you - " + nm
    return greet


# print(sayHi('Ravi Ranjan'))
# print(sayHi('Simran'))
a = sayHi('Amit Kumar')
print(a)
b = sayHi('chandan kumar')
print(b)

gm = "Good morning "
print(gm+sayHi("Kundan"))
