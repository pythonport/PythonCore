'''
Created on Sep 18, 2023
Program to calculate BMI (Body Mass Index) of a person
@author: Admin
'''
wkg = float(input('Enter weight in KG - '))
hmtr = float(input('Enter height in Meters - '))
bmi = wkg/(hmtr*hmtr)
print('BMI is - ', bmi)