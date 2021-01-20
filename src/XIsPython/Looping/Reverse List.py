'''
Created on Jan 4, 2019
Program to reverse the string with own logic 
and using reverse() function
@author: Rajesh Kumar Jha
'''
x = eval(input("Enter a list - "))
print ("Your actual List - ",x)
n = []
for i in range(len(x)):
    n.append(x[-(i+1)])
x  = n
print ("Your reverse List - ",x)

x.reverse()
print("reverse n List is - ",x)
