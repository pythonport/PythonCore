'''
Created on Dec 30, 2024

@author: admin
'''
s = {'Amit':[92, 86, 64], 'Nagma':[65, 42, 43], 'Devid':[92, 90, 88]}

def showGrade(s) :
    marksList = s['Amit']
    sumMarks = 0
    for i in range(3) :
        sumMarks += marksList[i]
    
        