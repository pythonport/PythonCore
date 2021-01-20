'''
Created on Jan 8, 2021

@author: admin
'''
deposite = int(input("Enter Deposite amount - "))
time = float(input("Enter time in year - "))
rate = 0.0

percent5 = deposite<2000 and time>=2
percent7 = deposite>=2000 and deposite<6000 and time>=2
percent8 = deposite>6000 and time>=1
percent10 = time>=5

if percent5 :
    rate = 0.05
elif percent7 :
    rate = 0.07
elif percent8 :
    rate = 0.08
elif percent10 :
    rate = 0.1