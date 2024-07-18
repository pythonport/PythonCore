'''
Created on Apr 17, 2024
https://www.geeksforgeeks.org/program-sum-arithmetic-series/

Sum of arithmetic series 
           = ((n / 2) * (2 * a + (n - 1) * d))
           Where
               a - First term
               d - Common difference
               n - No of terms
               
@author: admin
'''
def sumAriSeries(a,d,n):
    sumAri = ((n / 2) * (2 * a + (n - 1) * d))
    return sumAri

def getNthTrem(a,d,n):
    nthTerm = a+(n-1)*d
    return nthTerm
    
firstTerm = 1
comDiff= 5
noOfTerms = 20

nthTerm = getNthTrem(firstTerm, comDiff, noOfTerms)
print('Nth term is - ',nthTerm)

sum1 = sumAriSeries(firstTerm, comDiff, noOfTerms)
print("sum of arithmetic expression is - ",sum1)