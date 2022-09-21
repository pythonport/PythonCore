'''
Created on Mar 7, 2022

@author: admin
'''
#first way of creating dictionary
emp = {}
emp['name'] = 'karan'
emp['id'] = '007'
emp['salary'] = 78000
print(emp)

#second way of creating dictionary by using dict constructor function
teacher = dict(name='amit', subject="computer science")
print(teacher)

#third way of creating dictionary by using dict constructor function
#and passing dictionary as paramenter
numval = dict({1:33, 2:44, 5:44, 6:76, 2:32})
print(numval)

#by using zip function
d4 = dict(zip(('name','salary'),('Ganga',90543)))
print(d4)

#by using list 
d5 = dict([['name','Rahul'],['salary',188543]])
print(d5)