'''
Created on Apr 15, 2019

@author: admin
'''
import math


def selfPow(a, b):
    print("power of ", b, " on ", a, " = ", a ** b)
    
# selfPow(4,5)  #Required or Mandatory or Positional
# selfPow(33,44) #Required or Mandatory or Positional


def getAreaC(r, pi=math.pi):
    print("PI value is - ", pi)
    print("Area of ", r, " = ", pi * r * r)
    
# getAreaC(4,3.14)
# getAreaC(4)


def getSI(p, r=4, t=5):   #default argument
    print("Principal amt - ", p)
    print("Interest Rate - ", r)
    print("Time in year - ", t)
    print("SI is - ",p * r * t / 100)
    print("="*30)


getSI(5000, 8, 15)  
getSI(10000) 
getSI(2000,6)

def calcTotalMarks(hi,en,mt,ch,ph):
    calcsum = hi+en+mt+ch+ph
    calcavg = calcsum/5
    print("Total Marks is - ",calcsum, " And average - ",calcavg)
    
calcTotalMarks(45, 34, 54, 45, 21)
calcTotalMarks(phy=87, en=23, ch= 45, hi=23, mt=44)
